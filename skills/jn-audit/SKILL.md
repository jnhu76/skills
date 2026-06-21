---
name: jn-audit
description: Analyze a software project's real boundaries — bugs, design boundaries, feature gaps, docs gaps, misuse, environment issues, debt, and contribution strategy. Short key for personal invocation.
---

# Project Boundary Auditor

## Purpose

This skill helps determine whether an observed behavior in a software project is a bug, design boundary, feature gap, documentation gap, environment issue, misuse, technical debt, architectural mismatch, contribution opportunity, or security-sensitive issue.

The goal is not to summarize the project, but to understand its real contract, failure modes, extension boundary, and contribution path.

---

## When to Use

Use when the user asks: "这个项目到底能不能用？", "这是 bug 还是边界？", "这个项目适合 fork 吗？", "它能不能作为我们项目的基础？", "我怎么真正理解这个项目？", "哪些问题适合提 issue / PR / 安全披露？"

---

## Core Principle

```
违反已有契约 = bug
超出现有契约 = 设计边界
合理但未实现 = 功能缺口
实现了但没写清楚 = 文档缺失
能跑但抽象别扭 = 设计债
OS/权限/依赖/版本失败 = 环境问题
调用方式不符合项目设计 = 误用
```

Separate: user expectation, docs commitment, config/schema hints, code support, test coverage, runtime behavior, maintainer intent.

Do not treat README claims as verified facts.

---

## Evidence Levels

Every judgment must be labeled:

| Level | Meaning |
|---|---|
| L0 Guess | Pure hypothesis, no evidence yet |
| L1 Docs Claim | Claimed by README/docs |
| L2 Config Schema | Supported by config/schema |
| L3 Code Path | Confirmed in source code |
| L4 Tests | Covered by tests |
| L5 Runtime Verified | Reproduced locally |
| L6 Maintainer Intent | Maintainer-confirmed intent |

Prefer L3-L5 for strong conclusions.

---

## Classification Rules

### Bug

A. Contract violation: docs say it should work, config/schema implies it, code has intended path, tests/maintainers expect it, minimal reproduction fails consistently.

B. Local internal contradiction: unreachable code, duplicate return, unsafe fallback, broken invariant, exception swallowing, mismatched serialization.

### Design Boundary

The project clearly does not attempt to support the behavior. The absence is intentional or follows naturally from the project model.

### Feature Gap

Reasonable need that the project does not currently implement. Does not automatically mean bug.

### Documentation Gap

Code supports something but docs do not explain it.

### Environment Issue

Failure depends on OS, filesystem, shell, permissions, dependency version, runtime, container, network, or database behavior.

### Misuse

User is using the project against its documented model.

### Technical Debt / Design Smell

Behavior works but abstraction is unstable, overly coupled, hard to extend, under-tested, or hard to reason about.

### Security-Sensitive Issue

Involves secrets, encryption keys, auth, permissions, sandbox escape, RCE, unsafe deserialization, sensitive data exposure, credential leakage. Must be disclosed privately first.

---

## Analysis Workflow

### Step 1: One-Sentence Positioning

Write: 这个项目本质上是 ______，不是 ______。

**Completion criterion**: A single sentence that distinguishes the project from nearby but incorrect categories.

### Step 2: Extract Core Abstractions

Identify main concepts. Classify as: core abstraction / secondary / missing / accidental.

**Completion criterion**: Table with abstraction, status, evidence level, and notes.

### Step 3: Contract Map

Create: Explicitly promised / Implicitly supported / Not promised / Ambiguous.

**Completion criterion**: All four categories have at least one entry.

### Step 4: Capability Map

Table: Capability | Docs | Config | Code | Tests | Runtime | Judgment.

**Completion criterion**: Each capability section has evidence from at least two source types.

### Step 5: Trace the Main Flow

Describe the main operation as a trace. Then ask where missing abstractions would fit.

**Completion criterion**: A diagram of the main flow, with fit analysis for each missing abstraction.

### Step 6: Boundary Tests

Suggest tests that reveal real boundaries. See `reference/BOUNDARY-TESTS.md` for template lists.

**Completion criterion**: At least 5 project-specific boundary tests identified.

### Step 7: Classify Observed Issues

For each issue: observed behavior, expected behavior, evidence, classification, confidence, reasoning, next action.

**Completion criterion**: Every user-reported issue classified with evidence level and confidence.

### Step 8: Fit for User's Goal

State user's goal explicitly. Map requirements to fit (yes/partial/no).

**Completion criterion**: Requirements table complete with what's missing.

### Step 9: Extension Judgment

Classify extension strategy: use as-is / configure / patch / wrap / fork / redesign.

Rule: Missing option = configure/patch. Missing module = patch/wrap. Missing abstraction = fork/redesign. Conflicting worldview = redesign.

**Completion criterion**: One clear strategy selected with rationale.

### Step 10: Contribution Plan

Use when the user wants to contribute upstream. For every issue, decide disclosure classification, PR slicing, first PR recommendation. See `reference/CONTRIBUTION-PLANNING.md`.

**Completion criterion**: First PR recommendation picked with justification.

---

## Important Rules

- Do not call something a bug without contract evidence.
- Do not treat README claims as verified facts.
- Separate user expectation from project commitment.
- Prefer concrete reproduction steps over opinions.
- Do not recommend public disclosure for security-sensitive issues.
- Do not claim runtime verification unless actually reproduced.
- Prefer small, reviewable, reversible PRs for upstream contribution.

---

## Reference Files

| File | Content |
|---|---|
| `reference/CONTRIBUTION-PLANNING.md` | Security disclosure, patchability, first PR rules |
| `reference/BOUNDARY-TESTS.md` | Generic and domain-specific boundary test lists |
| `reference/OUTPUT-FORMAT.md` | Full report template with all sections |
