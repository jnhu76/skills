---
name: jn-audit
description: Analyze a software project to determine its real boundaries, contracts, bugs, feature gaps, documentation gaps, misuse cases, environment issues, technical debt, extension risks, and upstream contribution strategy. Use when evaluating whether to use, configure, patch, wrap, fork, redesign, or contribute to a project. Short key for personal invocation.
---

# Project Boundary Auditor

## Purpose

This skill helps determine whether an observed behavior in a software project is:

* a bug
* a design boundary
* a feature gap
* a documentation gap
* an environment issue
* user misuse
* technical debt
* architectural mismatch
* contribution opportunity
* security-sensitive issue requiring private disclosure

The goal is not to summarize the project, but to understand its real contract, failure modes, extension boundary, and contribution path.

This skill should answer:

```text
这个项目真实承诺了什么？
它实际支持了什么？
它没有支持什么？
哪些问题值得修？
哪些问题不该碰？
哪些适合 PR？
哪些应该先 issue/discussion？
哪些必须私下安全披露？
最终应该 use as-is / configure / patch / wrap / fork / redesign？
```

---

## When to Use

Use this skill when the user asks things like:

* “这个项目到底能不能用？”
* “这是 bug 还是边界？”
* “这个项目适合 fork 吗？”
* “这个项目能不能作为我们项目的基础？”
* “它和我们的需求差在哪里？”
* “我怎么真正理解这个项目？”
* “它只是 sync tool，还是 control plane？”
* “这个现象是不是我用错了？”
* “我们怎么继续参与这个开源项目？”
* “这些问题哪些适合提 issue？”
* “哪些问题适合直接 PR？”
* “哪些问题应该私下安全披露？”
* “这个项目适合 patch、wrap 还是 fork？”

---

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
涉及密钥/鉴权/权限/敏感信息 = 先考虑安全披露
适合小范围修复且不改变架构 = PR 候选
需要维护者判断设计方向 = issue/discussion 候选
```

Separate:

```text
用户期待
项目文档承诺
配置/schema 暗示
代码实际支持
测试覆盖
运行时行为
维护者意图
```

Do not treat README claims as verified facts.

---

## Evidence Levels

Every judgment must be labeled with one of these evidence levels:

| Level                | Meaning                                                           |
| -------------------- | ----------------------------------------------------------------- |
| L0 Guess             | Pure hypothesis, no evidence yet                                  |
| L1 Docs Claim        | Claimed by README/docs                                            |
| L2 Config Schema     | Supported by config/schema/options                                |
| L3 Code Path         | Confirmed in source code                                          |
| L4 Tests             | Covered by tests                                                  |
| L5 Runtime Verified  | Reproduced locally                                                |
| L6 Maintainer Intent | Maintainer-confirmed contract or design intent, not runtime proof |

Prefer L3-L5 evidence for strong conclusions.

Important:

```text
Maintainer intent can clarify contract boundaries,
but it does not replace runtime verification.
```

Example:

```text
维护者说“我们不打算支持 X”：
可以证明 X 是设计边界。

维护者说“X 应该能跑”：
不能证明 X 真的能跑，仍然需要测试或 runtime verification。
```

---

## Classification Rules

### Bug

Classify as bug when either condition A or B is true.

#### A. Contract violation

At least 3 of the following are true:

1. Documentation says it should work.
2. Config/schema implies it should work.
3. Source code contains a path intended to support it.
4. Tests, issues, or maintainer comments suggest maintainers expect it to work.
5. A minimal reproduction fails consistently.

#### B. Local internal contradiction

The source code contains a clear internal contradiction, such as:

* unreachable code
* duplicate return
* inconsistent defaults between code and example config
* unsafe fallback violating the function's local contract
* broken invariant
* obviously dead branch
* exception swallowing that hides a required failure state
* mismatched serialization/deserialization expectation

Do not overuse this rule.
Use it for clear local defects, not broad architectural disagreements.

---

### Design Boundary

Classify as design boundary when the project clearly does not attempt to support the behavior.

Examples:

* A single-node tool does not support distributed clustering.
* A sync tool does not provide control-plane scheduling.
* A local CLI does not provide hosted multi-tenant permissions.
* A Docker Compose project does not promise Kubernetes-native deployment.

Use this when the absence is intentional or follows naturally from the project model.

---

### Feature Gap

Classify as feature gap when the need is reasonable, but the project does not currently implement it.

Examples:

* API exists but lacks a documented endpoint.
* A sandbox API exposes start/stop but not pause/resume.
* A CRD system lacks rollback.
* A task engine lacks retry policy customization.

Feature gap does not automatically mean bug.

---

### Documentation Gap

Classify as documentation gap when code supports something but docs do not explain it.

Examples:

* Environment variable exists in code but not in `.env.example`.
* WebSocket event exists but no protocol documentation exists.
* Integration exists but no usage guide exists.
* Supported mode is only discoverable by reading source code.

---

### Environment Issue

Classify as environment issue when failure depends on:

* OS behavior
* filesystem behavior
* shell behavior
* path separator
* permissions
* dependency version
* local runtime
* container backend
* database version
* Redis/MySQL availability
* network/DNS/proxy behavior

---

### Misuse

Classify as misuse when the user is using the project against its documented model.

Examples:

* Expecting stateful orchestration from a stateless gateway.
* Expecting local filesystem access from a hosted SaaS-only tool.
* Calling internal APIs as public APIs.
* Editing generated files that are documented as non-user-editable.

---

### Technical Debt / Design Smell

Classify as technical debt when the behavior works but the abstraction is:

* unstable
* overly coupled
* hard to extend
* under-tested
* difficult to reason about
* dependent on implicit conventions
* inconsistent with the project's own guidelines
* likely to cause future maintenance cost

Technical debt is not automatically a bug.

---

### Security-Sensitive Issue

Classify as security-sensitive when the issue involves:

* default secrets
* encryption keys
* token handling
* authentication
* authorization
* permission bypass
* privilege escalation
* sandbox escape
* remote code execution
* unsafe deserialization
* sensitive data exposure
* raw exception leakage
* credential leakage
* information disclosure
* audit/compliance risk

Security-sensitive issues may still be bugs, but the contribution path must be private-first unless already publicly acknowledged.

---

## Contribution Planning Rules

Use this section when the user wants to contribute upstream or decide how to participate in the project.

### Security Disclosure Rule

If an issue involves any of the following, do not recommend a public issue or public PR first:

* default secrets
* encryption keys
* authentication bypass
* authorization bypass
* token leakage
* raw exception leakage
* privilege escalation
* sandbox escape
* remote code execution
* unsafe deserialization
* sensitive data exposure
* user data exposure
* credential storage weakness
* audit/compliance vulnerability

For these cases, recommend private security disclosure first, unless the issue has already been publicly acknowledged by maintainers.

A private security disclosure should include:

```text
- short vulnerability summary
- affected component
- impact
- minimal reproduction or code evidence
- suggested fix direction
- whether the reporter is willing to help prepare a patch
```

Do not include exploit-style instructions unless necessary for maintainers to reproduce safely.

---

### Patchability Score

| Score | Meaning                                                        |
| ----- | -------------------------------------------------------------- |
| S     | Very small patch, <= 3 files, no behavior change outside scope |
| M     | Localized behavior change, needs tests                         |
| L     | Cross-module change, migration or compatibility risk           |
| XL    | Architecture-level change, not suitable for direct PR          |

Use this score to decide whether an issue should become:

```text
direct PR
public issue
discussion
private security advisory
future roadmap item
do not touch yet
```

---

### Acceptance Likelihood

| Level  | Meaning                                                                                             |
| ------ | --------------------------------------------------------------------------------------------------- |
| High   | Small, well-scoped, tested, aligned with project style                                              |
| Medium | Useful but may require maintainer preference or design discussion                                   |
| Low    | Large refactor, unclear value, risky migration, broad behavior change, or unclear maintainer intent |

Prefer high-acceptance PRs for early contribution.

---

### Public Contribution Rule

Prefer direct PR only when:

* the issue is not security-sensitive
* the scope is small
* the expected behavior is clear
* tests or docs can be added
* no migration is required
* no broad refactor is needed
* the PR can be reviewed independently
* the change fits existing abstractions

Use issue/discussion first when:

* the behavior may be intentional
* the fix changes public behavior
* multiple designs are possible
* the change touches core abstractions
* the project contract is ambiguous
* maintainers may need to choose direction
* the change may affect compatibility

Use private security disclosure first when:

* the issue may expose secrets, tokens, credentials, permissions, sandbox boundaries, or sensitive runtime details.

---

### First PR Rule

When recommending a first PR, pick exactly one.

The first PR should satisfy:

```text
- no security-sensitive disclosure
- touch <= 3 files
- include test or documentation update
- no broad refactor
- no behavior change outside stated scope
- easy to review
- easy to revert
```

Avoid making the first PR a large refactor, architectural redesign, or security-sensitive patch.

---

## Analysis Workflow

### Step 1: One-Sentence Positioning

Write:

```text
这个项目本质上是 ______，不是 ______。
```

The sentence should distinguish the project from nearby but incorrect categories.

Examples:

```text
这个项目本质上是一个 Kubernetes-inspired multi-agent orchestration platform，
不是简单的 chatbot framework，也不是 general-purpose workflow engine。
```

```text
这个项目本质上是一个 skill sync/install tool，
不是 agent control plane，也不是 permission runtime。
```

---

### Step 2: Extract Core Abstractions

Identify the project's main concepts.

Look for:

* source
* target
* skill
* rule
* command
* prompt
* mode
* sync
* install
* audit
* profile
* policy
* planner
* lockfile
* adapter
* rollback
* daemon
* executor
* sandbox
* workspace
* task
* model
* agent
* team
* namespace
* resource
* event
* queue
* subscription
* knowledge base
* permission
* audit log
* rate limit
* deployment mode

Then classify abstractions as:

```text
core abstraction
secondary abstraction
missing abstraction
accidental abstraction
```

Definitions:

| Status                 | Meaning                                                       |
| ---------------------- | ------------------------------------------------------------- |
| core abstraction       | The project cannot be understood without it                   |
| secondary abstraction  | Useful but not central                                        |
| missing abstraction    | Needed for the user's goal, but absent                        |
| accidental abstraction | Present in code, but orthogonal to the project’s core purpose |

Output:

```markdown
| Abstraction | Status | Evidence | Notes |
|---|---|---|---|
| ... | core/secondary/missing/accidental | Lx: ... | ... |
```

---

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

Rules:

* Explicitly promised means docs, README, API docs, or maintainer statements say it should work.
* Implicitly supported means config/schema/code paths strongly suggest intended support.
* Not promised means the project does not claim or imply support.
* Ambiguous means there is partial evidence but no clear contract.

Do not infer promises from user expectations.

---

### Step 4: Capability Map

Create a capability table:

```markdown
| Capability | Docs | Config | Code | Tests | Runtime | Judgment |
|---|---|---|---|---|---|---|
| ... | ✅/❌/? | ✅/❌/? | ✅/❌/? | ✅/❌/? | ✅/❌/? | bug/boundary/gap/docs/debt |
```

Rules:

* Do not treat docs alone as proof.
* Do not treat code alone as user-facing contract.
* A capability with code but no docs may be a documentation gap.
* A capability with docs but no code may be a feature gap or stale documentation.
* A capability with code and tests but poor abstraction may be technical debt.
* A capability with partial implementation and TODOs is usually a feature gap, not necessarily a bug.

---

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

For agent or orchestration projects, trace:

```text
user request
  ↓
frontend/API/websocket
  ↓
auth/access check
  ↓
task/session creation
  ↓
resolve agent/team/model/tool config
  ↓
build execution request
  ↓
dispatch to executor/sandbox/runtime
  ↓
stream events back
  ↓
persist state
  ↓
render result / notify user
```

Then ask:

```text
Where would policy fit?
Where would audit fit?
Where would rollback fit?
Where would adapter rendering fit?
Where would compatibility checking fit?
Where would permission enforcement fit?
Where would rate limiting fit?
Where would observability fit?
Where would recovery fit?
```

If no natural location exists, the requested feature may not fit the architecture.

---

### Step 6: Boundary Tests

Suggest tests that reveal real boundaries.

Use generic boundary tests first:

1. duplicate resource name
2. missing required config
3. invalid schema/frontmatter/metadata
4. broken dependency reference
5. source/resource deleted after previous sync or execution
6. target already has local edits or existing state
7. permission denied
8. partial operation failure
9. project config conflicts with global config
10. unsupported OS/path/runtime behavior
11. repeated operation idempotency
12. rollback after failed operation
13. concurrent operation on same resource
14. stale cache or stale lock
15. dependency unavailable at startup
16. dependency unavailable during operation
17. timeout during external call
18. cancellation during long-running operation
19. malformed external response
20. version mismatch between components

For skill/sync projects, specialize into:

1. duplicate skill name
2. missing `SKILL.md`
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

For agent/executor/sandbox projects, specialize into:

1. executor unavailable
2. sandbox startup failure
3. sandbox timeout
4. sandbox cancellation
5. workspace missing
6. workspace permission denied
7. callback lost
8. streaming disconnect
9. duplicate task message
10. concurrent task execution
11. stale distributed lock
12. dependency restart during execution
13. rate limiter backend unavailable
14. token expired during execution
15. tool call returns malformed result
16. model API timeout
17. event ordering mismatch
18. task recovery after process restart

---

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
- Maintainer intent: ...

**Classification:**  
bug / design boundary / feature gap / documentation gap / environment issue / misuse / technical debt / security-sensitive issue

**Confidence:**  
low / medium / high

**Reasoning:**  
...

**Suggested next action:**  
use as-is / file issue / patch / fork / wrap / avoid / private security disclosure / discussion first
```

Rules:

* Be specific.
* Avoid vague criticism.
* Explain why it is not another category.
* If evidence is only L3, do not claim runtime verification.
* If runtime is not reproduced, say so.
* If security-sensitive, do not recommend public issue first.

---

### Step 8: Fit for User's Goal

State the user's goal explicitly.

Example:

```text
User goal:
Build and operate an AI-native operating system for defining, organizing,
and running intelligent agent teams.
```

Then map requirements:

```markdown
| Requirement | Fit | Notes |
|---|---|---|
| ... | yes/partial/no | ... |
```

Rules:

* Separate the project's own goal from the user's goal.
* Do not assume the user’s goal is the project’s contract.
* If fit is partial, say what is missing.
* If fit requires patch/wrap/fork, explain why.

---

### Step 9: Extension Judgment

Classify extension strategy:

| Strategy  | Meaning                                     |
| --------- | ------------------------------------------- |
| Use as-is | Project already fits the need               |
| Configure | Need can be solved with config              |
| Patch     | Small localized code change                 |
| Wrap      | Keep project as backend, add external layer |
| Fork      | Core behavior needs sustained changes       |
| Redesign  | Abstractions do not fit target problem      |

Use this rule:

```text
Missing option = configure/patch
Missing module = patch/wrap
Missing abstraction = fork/redesign
Conflicting worldview = redesign
```

Examples:

```text
缺一个配置项 → configure/patch
缺一个 API endpoint → patch
缺一个外部 policy layer → wrap
缺核心权限模型 → fork/redesign
项目世界观完全不同 → redesign
```

---

### Step 10: Contribution Plan

Use this step when the user wants to contribute upstream.

For every issue, decide:

* whether it is safe to discuss publicly
* whether it should be reported privately as a security issue
* whether it is suitable for a direct PR
* whether it should first become an issue or discussion
* whether it is too large or risky for a first contribution
* how likely maintainers are to accept it
* whether it aligns with the user's long-term contribution direction

Output:

```markdown
## Contribution Plan

### Disclosure Classification

| Issue | Public Issue | Direct PR | Private Security Advisory | Reason |
|---|---:|---:|---:|---|
| ... | yes/no | yes/no | yes/no | ... |

### PR Slicing

| PR | Title | Scope | Files | Tests | Risk | Patchability | Acceptance Likelihood |
|---|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | low/medium/high | S/M/L/XL | High/Medium/Low |

### First PR Recommendation

Pick exactly one first PR.

Explain:

- why this PR first
- why it is safe to do publicly
- why it is likely to be accepted
- what files it should touch
- what tests/docs it should include
- what must not be included

### Do Not Do Yet

List valid issues that are not suitable for immediate contribution.

Explain why:

- security sensitivity
- migration risk
- architecture scope
- review burden
- unclear maintainer intent
- too many files touched
- high conflict risk
- requires design discussion
```

---

## Output Format

When using this skill, produce the following report.

# Project Boundary Audit: `<project name>`

## 1. One-Sentence Positioning

这个项目本质上是 ______，不是 ______。

---

## 2. Core Abstractions

| Abstraction | Status                                  | Evidence | Notes |
| ----------- | --------------------------------------- | -------- | ----- |
| ...         | core / secondary / missing / accidental | Lx: ...  | ...   |

---

## 3. Contract Map

### Explicitly promised

* ...

### Implicitly supported

* ...

### Not promised

* ...

### Ambiguous

* ...

---

## 4. Capability Map

| Capability |  Docs | Config |  Code | Tests | Runtime | Judgment |
| ---------- | ----: | -----: | ----: | ----: | ------: | -------- |
| ...        | ✅/❌/? |  ✅/❌/? | ✅/❌/? | ✅/❌/? |   ✅/❌/? | ...      |

---

## 5. Main Flow Trace

```text
...
```

### Where Missing Abstractions Would Fit

| Missing Abstraction    | Natural Fit?   | Location | Notes |
| ---------------------- | -------------- | -------- | ----- |
| policy                 | yes/no/partial | ...      | ...   |
| audit                  | yes/no/partial | ...      | ...   |
| rollback               | yes/no/partial | ...      | ...   |
| compatibility checking | yes/no/partial | ...      | ...   |

---

## 6. Observed Issues Classification

### Issue 1: ...

**Observed behavior:**
...

**Expected behavior:**
...

**Evidence:**

* Docs: ...
* Config/schema: ...
* Code path: ...
* Tests: ...
* Runtime: ...
* Maintainer intent: ...

**Classification:**
...

**Confidence:**
low / medium / high

**Reasoning:**
...

**Suggested next action:**
use as-is / file issue / patch / fork / wrap / avoid / private security disclosure / discussion first

---

## 7. Boundary Test Plan

1. ...
2. ...
3. ...

---

## 8. Fit for User's Goal

User goal:

```text
...
```

Project fit:

| Requirement | Fit            | Notes |
| ----------- | -------------- | ----- |
| ...         | yes/partial/no | ...   |

---

## 9. Final Judgment

Choose one:

* use as-is
* configure
* patch
* wrap
* fork
* redesign

Final answer:

```text
这个项目适合 ______，不适合 ______。
最稳妥路线是 ______。
```

---

## 10. Contribution Plan

### Disclosure Classification

| Issue | Public Issue | Direct PR | Private Security Advisory | Reason |
| ----- | -----------: | --------: | ------------------------: | ------ |
| ...   |       yes/no |    yes/no |                    yes/no | ...    |

---

### PR Slicing

| PR  | Title | Scope | Files | Tests | Risk            | Patchability | Acceptance Likelihood |
| --- | ----- | ----- | ----- | ----- | --------------- | ------------ | --------------------- |
| ... | ...   | ...   | ...   | ...   | low/medium/high | S/M/L/XL     | High/Medium/Low       |

---

### First PR Recommendation

Pick exactly one first PR.

Explain:

```text
Why this PR first:
...

Scope:
...

Files likely touched:
...

Tests/docs required:
...

Not included:
...
```

---

### Do Not Do Yet

| Issue | Why Not Now                                                                                            | Future Path                                      |
| ----- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| ...   | security sensitivity / migration risk / architecture scope / review burden / unclear maintainer intent | private advisory / discussion / later PR / avoid |

---

## Important Rules

* Do not praise the project generically.
* Do not call something a bug without contract evidence.
* Do not treat README claims as verified facts.
* Separate user expectation from project commitment.
* Separate feature absence from broken behavior.
* Prefer concrete reproduction steps over opinions.
* Always identify whether the requested capability fits the project's existing abstractions.
* Do not recommend public disclosure for security-sensitive issues.
* Do not recommend large refactors as first contribution.
* Do not collapse documentation gap, feature gap, and bug into one category.
* Do not claim runtime verification unless actually reproduced.
* Do not claim maintainer intent unless there is issue/PR/comment evidence.
* Prefer small, reviewable, reversible PRs for upstream contribution.
* If the issue requires migration or changes public behavior, recommend discussion first.
* If evidence is weak, say what evidence is missing.
