# Output Format

## Full Report Template

```markdown
# Project Boundary Audit: <project name>

## 1. One-Sentence Positioning

这个项目本质上是 ______，不是 ______。

## 2. Core Abstractions

| Abstraction | Status | Evidence | Notes |
|---|---|---|---|
| ... | core/secondary/missing/accidental | Lx: ... | ... |

## 3. Contract Map

### Explicitly promised
### Implicitly supported
### Not promised
### Ambiguous

## 4. Capability Map

| Capability | Docs | Config | Code | Tests | Runtime | Judgment |
|---|---|---|---|---|---|---|
| ... | ✅/❌/? | ✅/❌/? | ✅/❌/? | ✅/❌/? | ✅/❌/? | bug/boundary/gap/docs/debt |

## 5. Main Flow Trace

```text
...
```

### Where Missing Abstractions Would Fit

| Missing Abstraction | Natural Fit? | Location | Notes |
|---|---|---|---|
| ... | yes/no/partial | ... | ... |

## 6. Observed Issues Classification

### Issue 1: ...

**Observed behavior:** ...
**Expected behavior:** ...
**Evidence:** Docs / Config / Code / Tests / Runtime / Maintainer intent
**Classification:** bug / boundary / gap / docs / env / misuse / debt / security
**Confidence:** low / medium / high
**Reasoning:** ...
**Suggested next action:** use as-is / file issue / patch / fork / wrap / avoid / private disclosure

## 7. Boundary Test Plan

1. ...
2. ...
3. ...

## 8. Fit for User's Goal

User goal: ...
Project fit: ...

| Requirement | Fit | Notes |
|---|---|---|
| ... | yes/partial/no | ... |

## 9. Final Judgment

use as-is / configure / patch / wrap / fork / redesign

## 10. Contribution Plan

See reference/CONTRIBUTION-PLANNING.md for template.
```
