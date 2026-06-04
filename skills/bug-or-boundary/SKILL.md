---
name: bug-or-boundary
description: Quickly classify an observed project behavior as bug, design boundary, feature gap, documentation gap, environment issue, misuse, or technical debt.
---

# Bug or Boundary Classifier

## Purpose

This is a lightweight classifier for quickly judging whether an observed software behavior is a bug, a boundary, a missing feature, a documentation problem, an environment issue, misuse, or technical debt.

Use this when the user gives a concrete symptom and asks:

- “这是 bug 吗？”
- “这是项目边界吗？”
- “是不是我用错了？”
- “这个能不能提 issue？”
- “这个需要 patch 还是 wrap？”

## Core Rule

Use this formula:

```text
违反已有契约 = bug
超出现有契约 = design boundary
合理但未实现 = feature gap
实现了但没写清楚 = documentation gap
环境导致 = environment issue
用法不符合设计 = misuse
能跑但抽象别扭 = technical debt
```

## Evidence Checklist

Before classifying, check:

1. What did the docs/README promise?
2. What does the config/schema allow?
3. What does the code path suggest?
4. Are there tests for this behavior?
5. Has it been reproduced in a minimal case?
6. Is there an issue/PR/maintainer comment?

## Required Output

For each issue, output:

```markdown
## Issue: <name>

**Observed:**  
...

**Expected:**  
...

**Contract evidence:**  
- Docs:
- Config:
- Code:
- Tests:
- Runtime:
- Maintainer intent:

**Classification:** bug / boundary / gap / docs / env / misuse / debt

**Confidence:** low / medium / high

**Reasoning:**  
...

**Next action:** use / configure / file issue / patch / wrap / fork / redesign
```

## Important

Do not call something a bug unless there is evidence that the project promised or intended to support it.

If evidence is incomplete, say:

```text
当前只能判断为 hypothesis，不能定性为 bug。
```
