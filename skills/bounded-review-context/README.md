# bounded-review-context

## What this skill does

Use this skill **before requesting code review**.

It creates a scoped, impact-aware **Review Context Pack** for:

```text
superpowers/requesting-code-review
```

It should not do the final review.
It should not run tests.
It should not search the whole repository.

## Main idea

```text
Job Pack + current diff → Scope Lock → limited impact map → review pack
```

The most important rule is:

```text
Review follows the current diff impact chain. Context collection follows the Scope Lock.
```

## Typical command

```markdown
Use `bounded-review-context`.

Job / PR:
- Job ID: A01
- Job Pack: docs/phase1.7/api-contract/job_packs/A01-execution-pack.md
- Output: docs/phase1.7/api-contract/review_packs/A01-review-pack.md

Allowed context:
- Read the specified Job Pack.
- Read `git diff --stat`.
- Read `git diff --name-only`.
- Read only relevant changed-file diff hunks for this job.

Hard limits:
- Do not read unrelated phase documents.
- Do not search all phase directories.
- Do not run tests.
- Do not perform the final code review.
- Do not create a new phase directory if the requested output path looks wrong; report the mismatch.

Goal:
Generate a scoped Review Context Pack for `superpowers/requesting-code-review`.
```

## How it should behave on a narrow job

If the Job Pack says:

```text
Exactly one endpoint: POST /attempts/:attemptId/answers/:questionId
```

then the skill should not inspect other endpoints unless:

- the diff changes them
- changed code directly calls them
- the user explicitly asks to include them

It should not read unrelated phase documents such as:

```text
docs/phase1.4/
docs/phase1.5/
docs/phase1.6/
docs/phase1.8/
docs/phase2/
```

## Expansion trigger examples

Allowed expansion:

```text
The changed route imports a new helper from package X, and package X behavior is central to the response contract.
```

Not allowed expansion:

```text
This might be related to a previous phase, so I will inspect all old phase docs.
```

## Context7 review gate

The review pack must classify Context7 needs when the PR depends on external behavior:

- framework APIs
- ORM / DB APIs
- validation libraries
- route hooks / middleware
- SDK / OpenAPI / protocols
- test framework behavior
- auth/session/token libraries
- serialization / streaming / file upload behavior

During pack generation, do not perform deep Context7 research unless the user explicitly asks. Record whether evidence is already provided. If evidence is missing, the final reviewer must verify it and should request changes when required evidence is absent.

## Output path discipline

The Review Context Pack should stay in the same phase and same topic subtree as the Job Pack. Sibling directories are allowed, for example:

```text
input:  docs/phase1.7/api-contract/job_packs/A01-execution-pack.md
output: docs/phase1.7/api-contract/review_packs/A01-review-pack.md
```

If the Job Pack belongs to `phase1.7` but the requested output path is under `phase1.8`, and the user did not explain why, the skill must stop and report:

```text
Output Path Mismatch
```

It must not silently create a new phase directory.

## Size discipline

Keep the Review Context Pack compact: do not restate the full Job Pack, do not copy large diff hunks, list only relevant changed files, keep the impact map minimal, and keep Regression Proof Required short unless the job is genuinely complex.

## What good output looks like

A good Review Context Pack includes:

- PR intent
- Scope Lock
- context budget used
- Context7 Evidence Gate
- changed surface table
- minimal impact map
- contract / invariant checklist
- pollution risks
- boundary drift suspicion
- regression proof required
- required reviewer output format
- handoff to `superpowers/requesting-code-review`

## What this skill must avoid

Do not let the agent:

- perform final review while generating context
- run tests
- run typecheck
- browse full git history
- grep the whole repo without trigger
- read old review profiles by default
- read unrelated phase directories
- create phase directories automatically
- expand current PR fix scope because of curiosity
- treat historical debt as a blocker

## Handoff

After the Review Context Pack is generated, run:

```text
superpowers/requesting-code-review
```

The reviewer should review along the current diff impact chain only.
