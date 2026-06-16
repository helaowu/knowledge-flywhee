"""
Pre-Compact Save Hook

在对话上下文压缩之前，自动提取关键信息存入文件。
防止长对话后半段"忘记"前半段确认的东西。

安装：
1. 复制到 ~/.claude/hooks/precompact_save.py
2. 在 settings.json 中配置：
   {
     "hooks": {
       "PreCompact": [
         {"type": "command", "command": "python ~/.claude/hooks/precompact_save.py"}
       ]
     }
   }

原理：
- 触发时机：上下文即将被压缩
- 行为：分析当前会话内容，提取值得保留的信息
- 输出：追加到 raw_log.md 或对应的 memory 文件
"""

import json
import sys
import os
from datetime import datetime

def main():
    # 读取 hook 输入
    hook_input = json.loads(sys.stdin.read()) if not sys.stdin.isatty() else {}

    # 获取 memory 目录路径（需要根据你的项目配置修改）
    # 默认路径格式：~/.claude/projects/{project-slug}/memory/
    memory_dir = os.environ.get(
        "MEMORY_DIR",
        os.path.expanduser("~/.claude/projects/default/memory")
    )
    raw_log_path = os.path.join(memory_dir, "raw_log.md")

    # 确保目录存在
    os.makedirs(memory_dir, exist_ok=True)

    # 写入一条压缩标记
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n## [{timestamp}] | 系统 | pre-compact 存档触发\n"
    entry += "- 内容：上下文即将压缩，请在下一轮交互中检查是否有遗漏的关键信息\n"
    entry += "- 状态：system\n\n"

    with open(raw_log_path, "a", encoding="utf-8") as f:
        f.write(entry)

    # 输出提示给 AI（会注入到压缩后的上下文中）
    message = (
        "[PreCompact-Hook] 上下文即将压缩。"
        "请检查本次对话中是否有值得记录的内容（纠正、口径确认、偏好表达等），"
        "有的话写入 raw_log.md。"
    )

    print(json.dumps({"message": message}))

if __name__ == "__main__":
    main()
