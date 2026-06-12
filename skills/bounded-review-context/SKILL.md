---
name: bounded-review-context
description: 在请求代码审查前使用，为当前 PR / diff 生成 scoped, impact-aware Review Context Pack；沿当前改动影响链提示 reviewer，但严格限制上下文搜索、禁止全仓库考古和最终审查。
---

# Bounded Review Context

## Overview

This skill is a pre-review context generator for:

```text
superpowers/requesting-code-review
```

It does **not** perform the final code review.
It does **not** fix code.
It does **not** run tests.
It only generates a scoped, impact-aware **Review Context Pack**.

The pack helps the reviewer check:

- upstream callers affected by the current diff
- downstream consumers affected by the current diff
- contract changes
- data-flow changes
- side-effect changes
- pollution risk
- regression proof
- Context7 evidence for external API / framework / ORM / protocol behavior

## Core Rule

```text
Review follows the current diff impact chain. Context collection follows the Scope Lock.
```

Boundary does **not** mean “only look at changed files”.
Boundary means:

- reviewer may follow the current diff's real impact chain
- current PR bugs must be fixed
- current PR behavior must have tests or evidence
- historical debt must not block this PR
- unrelated issues must remain out of scope
- context search must not become full-repository archaeology

## Role Boundary

This skill only prepares review context.

It must not:

- complete the final review
- produce final reviewer findings as the answer
- decide whether the PR is mergeable
- run tests / typecheck / build / lint
- search the whole repository
- read unrelated phase documents
- create new phase directories automatically

If the user asks for a review pack, generate a review pack.
If the user asks for final review, use the review pack first, then hand off to `superpowers/requesting-code-review`.

## Mandatory Scope Lock

After reading the Job Pack / PR description, immediately derive a **Scope Lock**.

The Scope Lock must include:

- Job / PR ID
- primary endpoint / module / behavior
- explicit secondary checks
- explicit non-goals
- allowed / likely files
- conditional files
- forbidden endpoints / modules / phases / documents
- requested output path sanity check

Once the Scope Lock is derived, all context collection must obey it.

If the Job Pack says **exactly one endpoint**, do not inspect other endpoints unless:

1. the current diff modifies them, or
2. the changed code imports / calls them directly, or
3. the user explicitly asks to include them.

Phase documents outside the Job Pack's phase are out of scope by default.
Do not read them just because they exist in the repository.

## Context Budget

Default allowed context:

1. user-specified Job Pack / PR description / issue
2. `git diff --stat`
3. `git diff --name-only`
4. changed-file diff hunks related to the Scope Lock
5. user-provided test results
6. user-provided Context7 Evidence
7. user-provided non-goals

Default forbidden context:

- all other phase directories
- old review profiles
- old PR boundary documents
- full git history
- full repository grep
- unrelated source files
- unrelated docs
- full chat history

## Expansion Trigger Rule

You may expand context beyond the budget only with direct evidence.

Allowed triggers:

- a changed file imports or calls a module not listed in the Job Pack
- a changed test references old compatibility behavior
- a changed API response affects a known caller listed in the Job Pack
- the diff includes files outside allowed / likely files
- the user explicitly names an extra document, phase, endpoint, or module
- a contract change cannot be mapped without one directly referenced type or caller

Not allowed triggers:

- “This might relate to another phase.”
- “There may be historical context.”
- “I should understand the whole plan first.”
- “The repository has phase documents.”
- “A deleted file mentions an old phase.”
- “Reviewer may want more background.”

When expansion is triggered, document it:

```markdown
Expansion Trigger:
- Evidence:
- Extra context inspected:
- Why it is still inside the current PR impact chain:
```

## Output Directory Discipline

The Review Context Pack should stay in the **same phase** and the **same topic subtree** as the input Job Pack / PR document.

Sibling directories are allowed when they remain under the same phase and topic subtree.

Examples:

- Input Job Pack: `docs/phase1.7/jobs/A01-execution-pack.md`
- Output Review Pack: `docs/phase1.7/jobs/A01-review-pack.md`
- Input Job Pack: `docs/phase1.7/api-contract/job_packs/A01-execution-pack.md`
- Output Review Pack: `docs/phase1.7/api-contract/review_packs/A01-review-pack.md`

Rules:

- derive output path from the input document's phase and topic subtree
- sibling directories such as `job_packs/` and `review_packs/` are acceptable
- do not create new phase directories automatically
- do not relocate output to a different phase or unrelated directory
- if the user requests output in a different phase without a clear explanation, report `Output Path Mismatch` and suggest a reasonable path under the same phase

## Output Path Sanity Check

If the requested output path conflicts with the Job Pack phase or PR scope, stop and report:

```text
Output Path Mismatch
```

Example:

- Job Pack: `docs/phase1.7/.../A01-execution-pack.md`
- Requested output: `docs/phase1.8/.../A01-review-pack.md`
- `docs/phase1.8` does not exist and user did not explain why

Correct behavior:

- do not create `phase1.8`
- report the mismatch
- suggest the likely path under `phase1.7`

## Context7 Review Gate

If the PR touches external behavior, the reviewer must check Context7 evidence.

Context7 is required for:

- external libraries / frameworks
- ORM / database behavior
- transaction / lock / isolation / concurrency
- route / middleware / hook behavior
- validation schema behavior
- SDK / MCP / OpenAPI / protocol contract
- serialization / JSON parsing / streaming / multipart / file upload
- testing framework / mock / fixture / runner behavior
- build tools / package manager / config loader
- auth / session / token / permission libraries

During Review Context Pack generation, do not perform deep Context7 research unless the user explicitly asks.
Only classify required Context7 topics and record whether evidence was already provided.
The final reviewer must verify missing evidence before trusting external behavior.

If Context7 evidence is missing or unrelated, the Review Context Pack should instruct the final reviewer to mark:

```text
REQUEST CHANGES
```

Reason:

```text
This PR depends on external API / library / framework / protocol behavior, but the implementation lacks verified Context7 evidence.
```

The pack may still note obvious visible risks, but should not perform deep final review itself.

## Size Discipline

Prefer a compact pack.

- do not restate the full Job Pack
- do not copy large diff hunks
- Changed Surface only lists relevant changed files
- Impact Map must be minimal
- Regression Proof Required should default to 5-10 lines unless the task is genuinely complex
- do not turn the Review Context Pack into a paper

## Inputs

Try to collect:

- Job Pack / PR description / issue
- branch name
- base SHA / head SHA, if already available
- `git diff --stat`
- `git diff --name-only`
- relevant diff hunks
- test results, if already provided
- Context7 Evidence, if already provided
- known non-goals
- requested output path

If information is missing, continue with a `Missing Information` section.
Do not invent facts.

## Work Steps

### 1. Write PR Intent

State:

- goal
- original problem
- expected behavior
- non-goals

### 2. Derive Scope Lock

State:

- primary target
- secondary checks
- in scope
- out of scope
- allowed / likely files
- conditional files
- forbidden context expansion
- output path sanity check

### 3. Check Context Budget

State what context was used and what was intentionally not inspected.

If extra context was inspected, include the expansion trigger.

### 4. Check Context7 Evidence Gate

State:

- Context7 required: YES / NO / UNCLEAR
- reason
- evidence present or missing
- final reviewer action

### 5. Analyze Changed Surface

Use a table:

| File | Changed behavior | Why it matters | Review focus |
| --- | --- | --- | --- |

Do not copy the whole diff.
Only explain why the file matters to the current Scope Lock.

### 6. Build Impact Map

Do not draw a whole-system map.
Only map the current PR path.

For example:

```text
external input
  -> route / handler
  -> contract / validation
  -> domain / service
  -> storage / queue / external service
  -> response / side effect
  -> frontend / downstream consumer
```

### 7. List Contract / Invariant Checkpoints

Depending on the PR, include checks for:

- HTTP status
- request body
- response shape
- JSON keys
- code / reason
- message source
- serialization
- database write
- transaction / lock behavior
- queue / cache / external payload
- frontend state machine
- caller compatibility
- external API / framework behavior backed by Context7

### 8. List Pollution Risks

List only risks connected to the current diff.

Examples:

- unrelated route / module touched
- shared schema changed too broadly
- global error handler changed without scope
- frontend API client changed beyond caller
- database seed / transaction pollution
- tests depend on shared state
- OpenAPI / docs drift
- external payload keys drift
- auth / tenant / permission boundary affected
- mock / fixture does not match real framework behavior
- validation weakened to pass tests

### 9. Define Regression Proof Required

Use:

| Risk | Required test / evidence | Required assertion |
| --- | --- | --- |

The evidence can be:

- unit test
- integration test
- API contract test
- e2e test
- concurrency test
- migration / seed verification
- Context7 Evidence
- manual reproduction note
- targeted diff check

Do not run tests here.
Only state what evidence the final reviewer should require.

### 10. Generate Reviewer Instructions

Require the final reviewer to output:

| File / location | Issue | Severity | Introduced by current PR? | Blocking? | Suggested handling |
| --- | --- | --- | --- | --- | --- |

Severity:

- Critical
- Important
- Minor

Blocking rules:

- correctness / security / data-integrity / contract bugs introduced by this PR: blocking
- current PR behavior lacking test proof: blocking or important
- missing Context7 evidence for required external behavior: blocking
- unverified risk inside current impact chain: request test or evidence
- historical debt: record only, not blocking
- unrelated issue: out of scope

## Output Format

```markdown
# Review Context Pack: <branch / PR / Job>

## 0. Agent Directives

> Read before any review action.

### Pre-flight

- This Review Context Pack is the boundary and entry context.
- Use only the files, diffs, and evidence allowed by this pack.
- Do not use chat history or unrelated repository context.
- Read Scope Lock (section 2) before reviewing any file.
- Start with files listed in Changed Surface (section 5) and Impact Map (section 6).
- To inspect any additional file, first document a valid Expansion Trigger.
- Additional file inspection is allowed only when it remains inside the current PR impact chain.

### Hard limits

- Do not inspect additional files without a documented valid Expansion Trigger.
- Do not inspect files outside the current PR impact chain.
- Do not read other phase directories.
- Do not read full git history.
- Do not read old review profiles.
- Do not read chat history.
- Do not perform final review beyond the Scope Lock.

### Allowed context

- Files in Changed Surface table (section 5).
- Files in Impact Map (section 6) that are inside Scope Lock.
- Context7 evidence listed in section 4.

### Context7 actions

Before reviewing external behavior, call Context7 for each topic listed in Context7 Evidence Gate (section 4). If Context7 is required but evidence is missing, mark as blocking in Required Reviewer Output (section 11).

### Expansion rule

If you need to review a file NOT in the lists above:

1. State the trigger (import/call from changed file).
2. Verify trigger is valid per Expansion Trigger Rule (section 3).
3. Document in Scope Lock Compliance Check (section 14).

### Violation protocol

If any boundary is violated:

1. STOP immediately.
2. Log in Scope Lock Compliance Check (section 14).
3. Mark Compliance Verdict as NO.

## 1. PR Intent

- Goal:
- Original problem:
- Expected behavior:
- Non-goals:

## 2. Scope Lock

- Primary target:
- Secondary checks:
- In scope:
- Out of scope:
- Allowed / likely files:
- Conditional files:
- Forbidden context expansion:
- Output path sanity check:

## 3. Context Budget Used

### Used

-

### Intentionally Not Inspected

-

### Expansion Triggers

-

## 4. Context7 Evidence Gate

- Context7 required: YES / NO / UNCLEAR
- Reason:

| Topic | Needs Context7? | Evidence present? | Gap | Reviewer action |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 5. Changed Surface

| File | Changed behavior | Why it matters | Review focus |
| --- | --- | --- | --- |
|  |  |  |  |

## 6. Impact Map

### Upstream Callers

| Caller | How it reaches this change | Risk |
| --- | --- | --- |
|  |  |  |

### Downstream Consumers

| Consumer | What it receives / depends on | Risk |
| --- | --- | --- |
|  |  |  |

### Minimal Call Chain / Data Flow

```text
...
```

## 7. Contract / Invariant Checklist

-

## 8. Pollution Risk Checklist

-

## 9. Boundary Drift Suspicion

-

## 10. Regression Proof Required

| Risk | Required test / evidence | Required assertion |
| --- | --- | --- |
|  |  |  |

## 11. Required Reviewer Output

| File / location | Issue | Severity | Introduced by current PR? | Blocking? | Suggested handling |
| --- | --- | --- | --- | --- | --- |

## 12. Missing Information

-

## 13. Handoff

Use `superpowers/requesting-code-review` with this Review Context Pack.

Do not use the full conversation history as review context.
Review along the current diff impact chain only.
Do not search unrelated phase documents.
Do not force unrelated historical debt into this PR.
Do not perform final code review inside this pack generation step.

## 14. Scope Lock Compliance Check

This section is mandatory. The downstream reviewer uses it to verify boundary integrity.

### Files Read

| File | Inside Scope Lock? | Reason |
| --- | --- | --- |
|  |  |  |

### Expansion Triggers Used

| Trigger | Evidence | Still inside PR impact chain? |
| --- | --- | --- |
|  |  |  |

### Forbidden Context Accessed

- NONE / list each violation

### Compliance Verdict

- All context within Scope Lock: YES / NO
- Violations found: NONE / list
- Impact on review integrity: NONE / list
```

## Forbidden Behavior

This skill must not:

- perform final code review
- fix code
- edit tests
- process review comments
- run tests / typecheck / build / lint
- run broad grep without a trigger
- read unrelated phase directories
- read old review profiles by default
- read old PR boundary docs by default
- search full git history by default
- create output directories that contradict the job phase
- store Review Context Pack outside the Job Pack's phase and topic subtree
- relocate output to a different phase directory without user explicit request and clear explanation
- copy complete chat history
- copy full risk profiles
- turn historical debt into a current PR blocker
- treat boundary as “only changed files”
- expand current PR fix scope for reviewer curiosity
- forgive missing Context7 evidence when external behavior is central

## Final Rule

```text
Review along the current diff impact chain. Fix within PR boundary. Search only within the Scope Lock.
```
