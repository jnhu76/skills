---
name: construction-kickoff-supervisor
description: 在开始实现一个 Job 前使用，把 Job Card / 计划文档转成 TDD-ready Job Pack，明确边界、Context7 证据、风险、测试切片和停工条件。
origin: hoooo.org
---

# Construction Kickoff Supervisor

## Overview

This skill is a pre-construction supervisor.

It does **not** write code, modify tests, review diffs, or fix bugs.
It only turns a Job Card / issue / plan document into a **TDD-ready Job Pack**.

The Job Pack is then handed to:

```text
superpowers/test-driven-development
```

## Core Rule

```text
No TDD-ready Job Pack, no implementation.
```

The implementation agent must not take a long planning document and freely improvise.
It must receive a scoped Job Pack, then start TDD slice by slice.

## When To Use

Use this skill before implementation when the job involves:

- API contract
- database behavior, transaction, lock, isolation, or concurrency
- auth, permission, security, or tenant boundary
- frontend/backend protocol
- OpenAPI / SDK / external protocol
- validation schema
- cross-package modification
- long or ambiguous phase documentation
- a job where the coding agent may read too broadly or implement too much

Usually skip it for:

- one-line config change
- pure copy or wording change
- tiny fix with an already explicit failing test
- refactor with no external behavior and no contract impact

## Mandatory Scope Lock

Before generating TDD slices, derive a **Scope Lock** from the job input.

The Scope Lock must include:

- Job ID
- primary endpoint / module / behavior
- explicit secondary checks
- explicit non-goals
- allowed / likely files
- forbidden endpoints / modules / phases / documents
- output path, if the user specified one

Once the Scope Lock is written, every later section must obey it.

If the job says **exactly one endpoint**, do not include other endpoints except as explicit secondary checks.

## Output Directory Discipline

The Job Pack should stay in the **same phase** and the **same topic subtree** as the input Job Card / plan document.

Sibling directories are allowed when they remain under the same phase and topic subtree.

Examples:

- Input Job Card: `docs/phase1.7/jobs/A01-job-card.md`
- Output Job Pack: `docs/phase1.7/jobs/A01-job-pack.md`
- Input Job Card: `docs/phase1.7/api-contract/job_cards/A01.md`
- Output Job Pack: `docs/phase1.7/api-contract/job_packs/A01-execution-pack.md`

Rules:

- derive output path from the input document's phase and topic subtree
- sibling directories such as `job_cards/` and `job_packs/` are acceptable
- do not create new phase directories automatically
- do not relocate output to a different phase or unrelated directory
- if the user requests output in a different phase without a clear explanation, report `Output Path Mismatch` and suggest a reasonable path under the same phase

If the user-provided output path contradicts the job phase without a clear explanation, stop and report `Output Path Mismatch` instead of creating a new phase directory.

## Context Budget

Default context collection is limited to:

1. the user-provided Job Card / issue / plan
2. directly referenced design docs
3. directly referenced current failure report, if any
4. directly referenced endpoint inventory, if this is an API job
5. explicitly provided test commands
6. user-stated non-goals

Do **not** search the whole repository by default.
Do **not** read unrelated phase documents.
Do **not** load full chat history as implementation context.

## Expansion Trigger Rule

You may request or inspect additional context only when there is a direct trigger:

- the Job Pack references a specific file or document
- the target file imports a module whose behavior is central to the job
- the job modifies a contract with known callers
- the job explicitly says to check compatibility
- the user explicitly names another document, phase, module, or endpoint
- the first TDD slice cannot be defined because a concrete rule is missing

Not allowed triggers:

- “This may be related to another phase.”
- “I should understand the whole roadmap first.”
- “There may be historical context.”
- “The repository contains phase documents.”
- “A previous review profile may be useful.”

## Context7 Gate

Before implementation, determine whether Context7 is required.

Context7 is **required** when the job touches:

- external libraries or frameworks
- ORM / database API behavior
- transaction, lock, isolation, or concurrency behavior
- route / middleware / hook behavior
- validation schema behavior
- SDK / MCP / OpenAPI / protocol contract
- serialization / JSON parsing / streaming / multipart / file upload
- testing framework / mock / fixture / runner behavior
- build tools / package managers / config loaders
- auth / session / token / permission libraries

Context7 may be skipped only when:

- the change is purely project-local logic
- no external API behavior is involved
- the implementation follows a nearby existing project pattern
- the Job Pack explicitly explains why Context7 is unnecessary

The output must include:

```markdown
## Context7 Evidence Gate

- Context7 required: YES / NO / UNCLEAR
- Reason:

| Topic | Library / API / Protocol | Suggested Context7 query | Required evidence | Implementation impact |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
```

If Context7 is required but evidence is missing, still generate the Job Pack structure.
However, the Job Pack status must be:

```text
Blocked: Context7 evidence missing
```

Do not hand off to TDD while blocked.
List the specific Context7 topics / queries / evidence that must be supplied.
Only after the user or supervisor supplies the missing evidence may the Job Pack be marked TDD-ready.

## Size Discipline

Prefer a compact Job Pack.

- do not restate the full phase plan
- do not copy long background docs
- TDD slices should default to 3-7 items
- Common Failure Modes should default to 5-10 items
- Stop Conditions should default to 5-10 items
- do not turn the Job Pack into a paper

## Inputs

Use or ask for:

- Job Card / issue / phase plan
- relevant design document named by the user
- endpoint inventory, for API jobs
- current failure report, if any
- test commands
- user-stated non-goals
- intended output path, if any

If information is missing, do not invent it.
Write a `Missing Information` section.

## Work Steps

### 1. Confirm Job Intent

Write:

- Job ID
- Job name
- problem being solved
- expected system behavior after completion
- non-goals

### 2. Derive Scope Lock

Write:

- primary target
- secondary checks
- in scope
- out of scope
- allowed / likely files
- forbidden expansion
- output path sanity check

### 3. Check Context7 Requirement

Classify Context7 as:

- `YES`
- `NO`
- `UNCLEAR`

If `YES`, list exact libraries / APIs / protocols to verify, plus required Context7 topics / queries / evidence.
If required evidence is missing, set Job Pack status to `Blocked: Context7 evidence missing`.
If `NO`, justify why the job is project-local.
If `UNCLEAR`, list the missing information.

### 4. Confirm Final Target

For API jobs, specify:

- endpoint list
- HTTP status
- response shape
- JSON keys
- code / reason
- message source
- details security boundary
- frontend impact

For database / concurrency jobs, specify:

- protected invariant
- transaction boundary
- serialization point
- possible interleavings
- proof strategy

For security jobs, specify:

- baseline vs full hardening
- error response shape
- login / seed / dev-flow impact
- token / password / internal-error leakage boundary

### 5. Generate TDD Slices

Each slice must contain:

- Red test
- Expected failure
- Implementation target
- Verification command

Slices must be small enough that the implementation agent can start with one red test.

### 6. List Common Failure Modes

List likely job-specific failure modes.

Examples for API contract jobs:

- two response shapes coexist
- old path and new path both accepted accidentally
- reason enum mixed with natural-language message
- route uses inline message instead of registry
- frontend still depends on old shape
- details leaks internal data
- 204 response accidentally returns JSON body
- tests pass by relaxing schema instead of preserving contract

### 7. Define Stop Conditions

Stop before implementation if:

- target response shape is not unique
- HTTP status is undecided
- code / reason enum conflicts
- non-goals conflict with scope
- Context7 is required but evidence is absent
- first red test is not tied to target behavior
- implementation requires deleting or weakening validation
- implementation requires unrelated module changes
- output path contradicts the job phase

## Output Format

```markdown
# TDD-ready Job Pack: <Job ID / Name>

- Status: TDD-ready / Blocked: Context7 evidence missing / Blocked: missing information

## 0. Agent Directives

> Read before any implementation action.

### Pre-flight

- This Job Pack is your ONLY context.
- Read Scope Lock (section 2) before writing any code.
- First file you touch MUST be a test file listed in Allowed / likely files.
- If no test file is listed, STOP and report that the Job Pack is not TDD-ready.
- Implementation files can be touched only after the first red test is written.

### Hard limits

- Do not read files not in Allowed / likely files list.
- Do not read other phase directories.
- Do not read full git history.
- Do not read chat history.
- Do not reinterpret the full document set freely.
- Do not expand beyond the Scope Lock.

### Allowed context

- Files in Allowed / likely files list (section 2).
- Context7 evidence listed in section 3.

### Context7 actions

Before starting implementation, collect Context7 evidence once for all topics listed in Context7 Evidence Gate (section 3). Before each TDD slice, reuse collected evidence. Call Context7 again only if the slice introduces a new external API / behavior not covered by existing evidence.

If Context7 evidence conflicts with the Final Target:

1. STOP.
2. Report the conflict.
3. Do not update the Final Target silently.
4. Ask the user / supervisor to revise the Job Pack.

### Expansion rule

If you need a file NOT in Allowed list:

1. State the trigger (import/call from changed file).
2. Verify trigger is valid per Expansion Trigger Rule.
3. Document in Scope Lock Compliance Check (section 10).

### Violation protocol

If any boundary is violated:

1. STOP immediately.
2. Log in Scope Lock Compliance Check (section 10).
3. Report to user before continuing.

## 1. Job Intent

- Goal:
- Expected behavior:
- Non-goals:

## 2. Scope Lock

- Primary target:
- Secondary checks:
- In scope:
- Out of scope:
- Allowed / likely files:
- Forbidden expansion:
- Output path sanity check:

## 3. Context7 Evidence Gate

- Context7 required: YES / NO / UNCLEAR
- Reason:

| Topic | Library / API / Protocol | Suggested Context7 query | Required evidence | Implementation impact |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 4. Final Target

### Contract / Invariant

-

### HTTP / JSON / State Rules

-

### code / reason / message

-

### Safety Rules

-

## 5. TDD Slices

### Slice 1: <name>

- Red test:
- Expected failure:
- Implementation:
- Verification:

### Slice 2: <name>

- Red test:
- Expected failure:
- Implementation:
- Verification:

## 6. Common Failure Modes

-

## 7. Stop Conditions

-

## 8. Missing Information

-

## 9. Handoff to TDD

Use `superpowers/test-driven-development` only when Status is TDD-ready.

If Status is `Blocked: Context7 evidence missing`, do not hand off to TDD. First collect the missing Context7 topics / queries / evidence listed in section 3.

Follow this Job Pack exactly.
Do not reinterpret the full document set freely.
Do not expand beyond the Scope Lock.
Start with Slice 1 red test.

## 10. Scope Lock Compliance Check

This section is mandatory. The downstream TDD agent and reviewer use it to verify boundary integrity.

### Files Read

| File | Inside Scope Lock? | Reason |
| --- | --- | --- |
|  |  |  |

### Expansion Triggers Used

| Trigger | Evidence | Still inside Job scope? |
| --- | --- | --- |
|  |  |  |

### Forbidden Context Accessed

- NONE / list each violation

### Compliance Verdict

- All context within Scope Lock: YES / NO
- Violations found: NONE / list
- Impact on Job Pack integrity: NONE / list
```

## Forbidden Behavior

This skill must not:

- write code
- edit tests
- fix bugs
- review diffs
- run tests / typecheck / build / lint
- create multiple complex modes
- require a separate long-lived documentation system
- load complete chat history as context
- pull historical debt into the current job
- search unrelated phase documents
- create new phase directories without explicit approval
- store Job Pack outside the Job Card's phase and topic subtree
- relocate output to a different phase directory without user explicit request and clear explanation
- generate an implementation plan when the target conflicts with non-goals

## Final Rule

```text
Job Pack first. TDD second. Scope Lock always.
```
