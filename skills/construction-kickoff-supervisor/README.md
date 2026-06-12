# construction-kickoff-supervisor

## What this skill does

Use this skill **before implementation**.

It turns a Job Card / issue / plan into a scoped **TDD-ready Job Pack** for `superpowers/test-driven-development`.

It should not code, edit tests, run CI, or review a diff.

## Main idea

```text
Long plan → Scope Lock → Context7 Gate → TDD slices → handoff to TDD
```

The most important rule is:

```text
No TDD-ready Job Pack, no implementation.
```

## Typical command

```markdown
Use `construction-kickoff-supervisor`.

Job:
- Job ID: A01
- Job Card: <path or pasted job card>
- Output: docs/phase1.7/api-contract/job_packs/A01-execution-pack.md
- Relevant docs: <only the docs named here>

Hard limits:
- Do not read unrelated phase documents.
- Do not search the whole repository.
- Do not run tests.
- Do not write code.
- Do not start implementation.

Goal:
Generate a TDD-ready Job Pack for `superpowers/test-driven-development`.
```

## When Context7 is required

Context7 must be required when the job depends on external behavior:

- framework APIs
- ORM / DB APIs
- route hooks / middleware
- validation libraries
- SDK / OpenAPI / protocols
- test runner / mocking behavior
- auth/session/token libraries
- serialization / streaming / file upload behavior

The Job Pack must contain a `Context7 Evidence Gate` section.
If evidence is missing, still generate the Job Pack structure, but mark status as:

```text
Blocked: Context7 evidence missing
```

Do not hand off to TDD until the missing Context7 topics / queries / evidence are supplied.

## Output path discipline

The Job Pack should stay in the same phase and same topic subtree as the Job Card. Sibling directories are allowed, for example:

```text
input:  docs/phase1.7/api-contract/job_cards/A01.md
output: docs/phase1.7/api-contract/job_packs/A01-execution-pack.md
```

If the user asks for a different phase without a clear explanation, report `Output Path Mismatch` and suggest a path under the same phase. Do not automatically create a new phase directory.

## TDD handoff discipline

The implementation agent must touch a test file first. If no test file is listed in Allowed / likely files, the Job Pack is not TDD-ready. Implementation files can be touched only after the first red test is written.

Before implementation, collect Context7 evidence once for all listed topics. Reuse it per slice and call Context7 again only when a slice introduces new external behavior.

If Context7 evidence conflicts with the Final Target, stop, report the conflict, and ask the user / supervisor to revise the Job Pack. Do not silently update the target.

## Size discipline

Keep the Job Pack compact: do not restate the full phase plan, do not copy long background docs, default to 3-7 TDD slices, 5-10 common failure modes, and 5-10 stop conditions.

## What good output looks like

A good Job Pack should answer:

- What exactly is the primary target?
- What is in scope?
- What is explicitly out of scope?
- Which files are likely affected?
- What external behavior needs Context7 evidence?
- What is the first red test?
- What command proves the first slice?
- When should the agent stop instead of improvising?

## What this skill must avoid

Do not let the agent:

- read every phase plan
- reinterpret the roadmap
- turn a small job into a broad refactor
- run tests before defining TDD slices
- change code while generating the Job Pack
- silently create new phase directories
- treat historical debt as current job scope

## Handoff

After the Job Pack is generated, start implementation with:

```text
superpowers/test-driven-development
```

The TDD agent should follow the slices exactly and start with Slice 1 red test.
