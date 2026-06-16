# Knowledge Flywheel — Codex Configuration

## Core Mechanism: raw_log → Rule Upgrade

This system makes AI get smarter with every use through automatic knowledge capture and rule promotion.

## Real-time Observation (raw_log)

During every conversation, automatically append to `memory/raw_log.md` when:
- User corrects a mistake
- A definition/rule is confirmed
- A reusable pattern is discovered
- User expresses a preference
- User confirms a good approach (positive reinforcement)

### Entry Format

```markdown
## [YYYY-MM-DD] | {type} | {title}
- Content: what happened
- Count: 1
- Upgrade target: {file path}
- Status: raw
```

### Rules
- Same issue already exists → update count, don't create new entry
- Count ≥ 3 → MUST upgrade to formal rule

## Knowledge Base Auto-Maintenance

After each task, check these 4 items:
1. New concept/data source encountered → add to wiki
2. Definition confirmed → append to relevant page
3. Pitfall discovered → append to `memory/lessons.md`
4. Reusable pattern → append to `memory/patterns.md`

## Rule Upgrade Process

When an entry reaches count ≥ 3, or when user triggers review:
1. Check if rule already exists (update, don't duplicate)
2. Generalize (express without referencing the specific trigger)
3. Make actionable ("do X" or "never Y", not "be careful")
4. Place correctly (domain → conventions; behavior → AGENTS.md; experience → memory)
5. Show user for confirmation before writing

## System File Update Constraint

Before modifying ANY memory/convention/config file:
1. Show the proposed change to user
2. Wait for explicit confirmation
3. Then write
