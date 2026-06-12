# jn-semantic skill

This Claude skill extracts semantics from technical systems, papers, benchmarks, APIs, runtimes, databases, storage systems, sandboxes, and agent workflows.

## Install

Copy this directory to:

```bash
.claude/skills/jn-semantic/
```

or:

```bash
~/.claude/skills/jn-semantic/
```

## Use

Ask Claude:

```text
Use the jn-semantic skill to analyze this system and find research gaps.
```

Example:

```text
请用 jn-semantic skill 分析 CubeSandbox：
1. 抽出第一性目标
2. 基本操作
3. 对象/状态/effect
4. 语义规则
5. 权衡面
6. 科研缝隙
7. 最小实验
```

## Core formula

```text
semantic = operation × object × state/condition → observable behavior / guarantee / violation / cost
```
