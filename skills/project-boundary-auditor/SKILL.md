---
name: project-boundary-auditor
description: Analyze a software project to determine its real boundaries, contracts, bugs, feature gaps, documentation gaps, misuse cases, environment issues, technical debt, and extension risks. Use when evaluating whether to use, patch, wrap, fork, or redesign a project.
---

# Project Boundary Auditor

## Purpose

This skill helps determine whether an observed behavior in a software project is:

- a bug
- a design boundary
- a feature gap
- a documentation gap
- an environment issue
- user misuse
- technical debt
- architectural mismatch

The goal is not to summarize the project, but to understand its real contract, failure modes, and extension boundary.

## When to Use

Use this skill when the user asks things like:

- “这个项目到底能不能用？”
- “这是 bug 还是边界？”
- “这个项目适合 fork 吗？”
- “这个项目能不能作为我们项目的基础？”
- “它和我们的需求差在哪里？”
- “我怎么真正理解这个项目？”
- “它只是 sync tool，还是 control plane？”
- “这个现象是不是我用错了？”

## Core Principle

Do not classify a behavior as a bug just because it does not match the user's expectation.

Use this rule:

```text
违反已有契约 = bug
超出现有契约 = 设计边界
合理但未实现 = 功能缺口
实现了但没写清楚 = 文档缺失
能跑但抽象别扭 = 设计债
因为 OS/权限/依赖/版本失败 = 环境问题
调用方式不符合项目设计 = 误用
```

## Evidence Levels

Every judgment must be labeled with one of these evidence levels:

| Level | Meaning |
|---|---|
| L0 Guess | Pure hypothesis, no evidence yet |
| L1 Docs Claim | Claimed by README/docs |
| L2 Config Schema | Supported by config/schema/options |
| L3 Code Path | Confirmed in source code |
| L4 Tests | Covered by tests |
| L5 Runtime Verified | Reproduced locally |
| L6 Maintainer Intent | Confirmed by issue/PR/maintainer comment |

Prefer L3-L5 evidence for strong conclusions.

## Classification Rules

### Bug

Classify as bug only when at least 3 of the following are true:

1. Documentation says it should work.
2. Config/schema implies it should work.
3. Source code contains a path intended to support it.
4. Tests or issues suggest maintainers expect it to work.
5. A minimal reproduction fails consistently.

### Design Boundary

Classify as design boundary when the project clearly does not attempt to support the behavior.

### Feature Gap

Classify as feature gap when the need is reasonable, but the project does not currently implement it.

### Documentation Gap

Classify as documentation gap when code supports something but docs do not explain it.

### Environment Issue

Classify as environment issue when failure depends on OS, permissions, dependency versions, filesystem behavior, or shell behavior.

### Misuse

Classify as misuse when the user is using the project against its documented model.

### Technical Debt / Design Smell

Classify as technical debt when the behavior works but the abstraction is unstable, overly coupled, or hard to extend.

## Analysis Workflow

### Step 1: One-Sentence Positioning

Write:

```text
这个项目本质上是 ______，不是 ______。
```

### Step 2: Extract Core Abstractions

Identify the project's main concepts.

Look for:

- source
- target
- skill
- rule
- command
- prompt
- mode
- sync
- install
- audit
- profile
- policy
- planner
- lockfile
- adapter
- rollback
- daemon

Then classify abstractions as:

```text
core abstraction
secondary abstraction
missing abstraction
accidental abstraction
```

### Step 3: Contract Map

Create a contract map:

```markdown
## Contract Map

### Explicitly promised

- ...

### Implicitly supported

- ...

### Not promised

- ...

### Ambiguous

- ...
```

### Step 4: Capability Map

Create a table:

| Capability | Docs | Config | Code | Tests | Runtime | Judgment |
|---|---|---|---|---|---|---|
| ... | ✅/❌/? | ✅/❌/? | ✅/❌/? | ✅/❌/? | ✅/❌/? | bug/boundary/gap |

Do not treat docs alone as proof.

### Step 5: Trace the Main Flow

Describe the main operation as a trace.

Example:

```text
command
  ↓
load config
  ↓
scan source
  ↓
parse skill metadata
  ↓
match target
  ↓
copy/symlink/merge
  ↓
write metadata
  ↓
report result
```

Then ask:

```text
Where would policy fit?
Where would audit fit?
Where would rollback fit?
Where would adapter rendering fit?
Where would compatibility checking fit?
```

If no natural location exists, the requested feature may not fit the architecture.

### Step 6: Boundary Tests

Suggest tests that reveal real boundaries.

Common boundary tests:

1. duplicate skill name
2. missing SKILL.md
3. invalid frontmatter
4. broken symlink
5. source deleted after previous sync
6. target already has local edits
7. audit failure
8. partial sync failure
9. project config conflicts with global config
10. unsupported OS/path behavior
11. repeated sync idempotency
12. rollback after failed sync

### Step 7: Classify Observed Issues

For every observed issue, output:

```markdown
### Issue: <short name>

**Observed behavior:**  
...

**Expected behavior:**  
...

**Evidence:**  
- Docs: ...
- Config/schema: ...
- Code path: ...
- Tests: ...
- Runtime: ...

**Classification:** bug / design boundary / feature gap / documentation gap / environment issue / misuse / technical debt

**Confidence:** low / medium / high

**Reasoning:**  
...

**Suggested next action:**  
use as-is / file issue / patch / fork / wrap / avoid
```

### Step 8: Extension Judgment

Classify extension strategy:

| Strategy | Meaning |
|---|---|
| Use as-is | Project already fits the need |
| Configure | Need can be solved with config |
| Patch | Small localized code change |
| Wrap | Keep project as backend, add external layer |
| Fork | Core behavior needs sustained changes |
| Redesign | Abstractions do not fit target problem |

Use this rule:

```text
Missing option = configure/patch
Missing module = patch/wrap
Missing abstraction = fork/redesign
Conflicting worldview = redesign
```

## Output Template

When using this skill, produce the following report:

```markdown
# Project Boundary Audit: <project name>

## 1. One-Sentence Positioning

这个项目本质上是 ______，不是 ______。

## 2. Core Abstractions

| Abstraction | Status | Evidence | Notes |
|---|---|---|---|
| source | core | ... | ... |
| target | core | ... | ... |
| policy | missing | ... | ... |

## 3. Contract Map

### Explicitly promised

- ...

### Implicitly supported

- ...

### Not promised

- ...

### Ambiguous

- ...

## 4. Capability Map

| Capability | Docs | Config | Code | Tests | Runtime | Judgment |
|---|---:|---:|---:|---:|---:|---|
| ... | ... | ... | ... | ... | ... | ... |

## 5. Main Flow Trace

```text
...
```

## 6. Observed Issues Classification

### Issue 1: ...

**Classification:**  
...

**Confidence:**  
...

**Reasoning:**  
...

**Next action:**  
...

## 7. Boundary Test Plan

1. ...
2. ...
3. ...

## 8. Fit for User's Goal

User goal:

```text
...
```

Project fit:

| Requirement | Fit | Notes |
|---|---|---|
| ... | yes/partial/no | ... |

## 9. Final Judgment

Choose one:

- use as-is
- configure
- patch
- wrap
- fork
- redesign

Final answer:

```text
这个项目适合 ______，不适合 ______。
最稳妥路线是 ______。
```
```

## Important Rules

- Do not praise the project generically.
- Do not call something a bug without contract evidence.
- Do not treat README claims as verified facts.
- Separate user expectation from project commitment.
- Separate feature absence from broken behavior.
- Prefer concrete reproduction steps over opinions.
- Always identify whether the requested capability fits the project's existing abstractions.
