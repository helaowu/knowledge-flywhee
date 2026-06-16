# knowledge-flywheel

**让 AI 越用越聪明的系统。不靠"下次注意"，靠机制。**

AI 的默认状态：今天踩的坑明天再踩一遍，纠正了说"好的"下次照犯，上下文一压缩之前聊的全忘。这个仓库用 6 个机制，把"犯过的错"变成"再也不会犯的规则"。

---

## 谁需要这个

| 你的情况 | 这个仓库能给你什么 |
|---------|---------------|
| AI 反复犯同样的错，你纠正了他但下次还犯 | 错题集 + 3 次自动升级规则——说 3 次就变成永久规则 |
| 长对话到后面 AI 开始忘前面的约定 | 压缩前存档 hook，关键信息不丢 |
| 换个新对话就从零开始 | 文件系统级记忆，跨会话持久化 |
| 做过的复杂流程每次都要重说一遍 | 自动沉淀为 skill/command，下次一键触发 |
| 觉得 AI 应该"越用越懂我"但实际没有 | 这套系统就是在解决这个问题 |

## 自动化 vs 复利：区别在哪

| 自动化 | 复利（这套系统） |
|-------|--------------|
| 每周跑一次周报脚本，省时间 | 每次跑完记下新发现，下次碰到同样的表直接有底 |
| 脚本不进步，你不改它永远一样 | 系统自己进步，每次使用都积累新知识 |
| 犯了错你手动改脚本 | 犯了错自动记录，3 次后自动变成规则 |
| AI 只是执行工具 | AI 是会长记性的协作者 |

## 6 个机制

```
对话中发生了值得记的事
    ↓
① 自动写入 raw_log（错题集）
    ↓
② 同一条目出现 3 次 → 升级为正式规则
    ↓
③ 写入 CLAUDE.md 或规范文件 → 以后所有对话自动遵守
```

| # | 机制 | 触发时机 | 解决什么 |
|---|------|---------|---------|
| 1 | 错题集（raw_log） | 对话中被纠正、确认口径、发现偏好 | 不靠记忆，落到文件 |
| 2 | 3 次升级规则 | 同一条目出现 3 次 | 确认是系统性问题，不是边界情况 |
| 3 | 笔记本自动生长 | 每次任务完成后 | 新发现自动入库 |
| 4 | 压缩前存档 | 上下文即将被压缩 | 关键信息不丢失 |
| 5 | 流程沉淀 | 完成了一个非平凡任务 | 下次一键复用 |
| 6 | 审查+升级 | 定期或手动触发 | 错题集清零，规则库生长 |

## 目录结构

```
.
├── docs/
│   ├── principles.md          ← 为什么需要这些机制
│   └── mechanisms.md          ← 每个机制的详细运作
├── claude-code/
│   ├── CLAUDE.md              ← 触发规则模板（什么时候记、什么时候升级）
│   ├── hooks/
│   │   └── precompact_save.py ← 压缩前自动存档
│   ├── commands/
│   │   └── review-memory.md   ← /review-memory skill
│   ├── memory/
│   │   ├── MEMORY.md          ← 记忆索引模板
│   │   └── raw_log.md         ← 错题集模板
│   └── wiki/                  ← 知识库模板
│       ├── index.md
│       ├── lessons/
│       └── patterns/
└── codex/
    ├── AGENTS.md
    └── memory/
```

## Quick Start

### Claude Code

```bash
# 1. 复制触发规则到你的项目 CLAUDE.md
cat claude-code/CLAUDE.md >> your-project/CLAUDE.md

# 2. 安装压缩前存档 hook
cp claude-code/hooks/precompact_save.py ~/.claude/hooks/

# 3. 安装 review-memory skill
cp claude-code/commands/review-memory.md ~/.claude/commands/

# 4. 初始化记忆目录
cp -r claude-code/memory/ ~/.claude/projects/your-project/memory/

# 5. 初始化知识库（可选）
cp -r claude-code/wiki/ your-project/wiki/
```

### Codex CLI

```bash
cp codex/AGENTS.md your-project/AGENTS.md
cp -r codex/memory/ your-project/memory/
```

## 效果是什么样的

装完跑一段时间后：
- 你的 `raw_log.md` 会积累你的纠正记录和偏好
- 出现 3 次的条目会被升级到 CLAUDE.md 成为正式规则
- AI 在新对话里自动遵守这些规则，不需要你重新说
- `wiki/` 里会积累你的领域知识（表结构、口径、常见坑）
- 做过的复杂任务会沉淀成 `/command`，下次一句话触发

## 相关项目

- [ai-data-team](https://github.com/helaowu/ai-data-team) — 多角色协作框架，跟本仓库配合使用

## License

MIT
