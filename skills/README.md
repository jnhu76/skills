# Skills Index

这里是所有 skill 的扁平导航。

## Skill List

| Skill | 用途 | 适合场景 |
|---|---|---|
| [`project-boundary-auditor`](project-boundary-auditor/) | 分析软件项目真实边界、契约、bug、功能缺口、文档缺失和扩展风险 | 判断项目能否作为基础；判断 use / patch / wrap / fork / redesign |
| [`bug-or-boundary`](bug-or-boundary/) | 快速判断一个现象是 bug、设计边界、功能缺口、文档缺失、环境问题、误用还是技术债 | 判断某个具体现象是否值得提 issue 或 patch |

## 文件约定

每个 skill 目录包含：

```text
<skill-name>/
├── SKILL.md    # agent 执行说明
└── README.md   # 人类导航与调用 prompt
```

## 命名规则

使用短横线命名：

```text
project-boundary-auditor
bug-or-boundary
cpp-build-debugger
go-service-debugger
agent-sandbox-reviewer
paper-reading-card
```

不要使用：

```text
Project Boundary Auditor
bug_or_boundary
bugOrBoundary
my skill
```

## 什么时候需要分类？

skill 少的时候，直接靠这个 README 表格就够了。

等 skill 变多，比如超过 20 个，再考虑增加：

```text
registry.yaml
tags
scripts
```
