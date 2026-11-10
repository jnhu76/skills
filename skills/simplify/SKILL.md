---
name: simplify
description: >
  Evidence-grounded simplification of working code. Use after a feature or bug fix,
  during PR review, or when asked to simplify, remove redundant defenses,
  reduce test-suite maintenance cost, or assess which tests deserve retention.
  Defaults to the current diff; preserves supported contracts and independent
  security, concurrency, transaction, and persistence boundaries.
  Risk-accepting test deletion requires separate authorization.
---

# Simplify — Evidence-Grounded Code Reduction

**Goal:** Make correct code easier to understand and maintain, with the smallest coherent change. Optimize for fewer concepts and lower lifetime cost, not fewer lines. **No change is a valid result.**

## Authority and execution mode

1. Read the repository's agent instructions first (`AGENTS.md`; `CLAUDE.md` may be a thin adapter). Follow the relevant Accepted ADR, domain contracts, and testing policy. This skill never overrides them.
2. Determine authorization: **review** is read-only; **apply** requires explicit permission to modify files. Do not commit, push, merge, or change protected resources unless separately authorized by the repository's rules.
3. Scope defaults to the current task or PR diff. For a PR, compare the correct merge base against the PR head; include staged and unstaged changes. Do not mistake `git diff HEAD` for the full PR diff. **When the user names a whole test suite or asks to reduce accumulated tests, that explicit scope overrides diff-only review: inspect relevant existing tests even when they were not changed by the PR.** Cluster by behavior and failure mechanism; expand to overlapping test files through evidence, not full-repo archaeology. Protect unrelated worktree changes.
4. Optional focus: `reuse`, `clarity`, `defenses`, `tests`, `test-portfolio`, `efficiency`, or a named function/module. `tests` finds evidence-backed redundancy; `test-portfolio` additionally reviews retention value and risk budget. Focus changes priority, never repository authority.

## Procedure

### 1. Establish behavioral authority

For each target, identify its owner, callers, side effects, invariants, errors, ordering, and relevant tests. Read adjacent implementations before proposing a new helper. Investigate history only if the rationale is unclear and material.

Before deleting a check or branch, ask:
- Which boundary or invariant does it enforce?
- Is the input already validated by a **trusted owner** at this exact boundary?
- Could untrusted input, races, state changes, persistence, or an independent caller bypass that owner?
- What observable behavior demonstrates equivalence if we remove it?

A TypeScript type alone is **not** a runtime proof of reachability. Values may enter through JavaScript callers, casts, deserialization, database hydration, partial state, or races. For an internal invariant, establish the full set of callers and an enforced trust boundary; a structural parser does not discharge authorization, domain, transactional, or temporal obligations.

**One authority is not one enforcement point.** A shared authorization rule may be implemented once and still require enforcement at several independent entrypoints. The same is true for authentication, state transitions, transactions, persistence constraints, and time/concurrency protocols.

### 2. Find candidates in four dimensions

- **Reuse:** Duplicate adapters, DTOs, helpers, error mappings, or local rewrites of existing repository/library functionality. Prefer one semantic owner; avoid a generic abstraction without demand.
- **Clarity:** Speculative extension points, wrapper chains, unnecessary indirection, nested control flow, confusing names, redundant comments, or compatibility code past its contractual retirement.
- **Redundant defenses:** Identify these concrete anti-patterns as **candidates, not automatic deletions**:
  1. **Repeated same-zone validation:** Internal functions rechecking nullability, type or format after a trusted runtime parser/owner already established the exact precondition. Independent public, domain, transaction or persistence boundaries may still require enforcement.
  2. **Optional-chain contagion:** `user?.id` or `a?.b?.c` on genuinely required internal structures, manufacturing downstream `undefined` branches. Retain optional access for real partial, asynchronous, or externally sourced states.
  3. **Silent phantom fallbacks:** `?? ''`, `?? 0`, `|| []` concealing a required invariant violation. Retain intentional UX defaults and documented recovery semantics.
  4. **No-value exception relays:** `try/catch` that merely logs or wraps an error without meaningful context, recovery, or stack/cause preservation. Retain necessary auditing, diagnostics, cleanup, and semantic error translation.
- **Efficiency:** Observably redundant queries, allocations, rendering, I/O, repeated setup, or test execution. Require measurement or a clear cost model before claiming a performance gain.

Use one reviewer by default. Parallel independent reviews are optional only for large, genuinely separable diffs; consolidate and deduplicate before changes.

### 3. Gate each proposed subtraction

Keep a candidate only when all are true:
1. The underlying responsibility and contract are understood.
2. Its complexity cost is material (comprehension, maintenance, correctness, or measured runtime).
3. The simpler alternative preserves **externally observable behavior for valid contract inputs and supported failure modes**, or a changed contract has been explicitly authorized. Behavior for a **proven unreachable, non-contractual** state, including its error type, need not be retained.
4. The change is small, cohesive, and within task scope.
5. There is an independent, proportionate verification signal.

**Proof obligation for removing a defensive branch:**
- Identify its actual callers, trust boundary, and authoritative runtime validator; or prove the internal call graph is closed and the invariant is established for every caller.
- Exclude realistic paths through untrusted input, JavaScript/casts, deserialization, persistence, partial initialization, and concurrent or asynchronous state changes. **Type declarations alone do not satisfy this proof.**
- Check that the branch is not a supported public failure mode, required diagnostic, recovery path, or independently enforced invariant.
- Run the relevant existing tests; use targeted negative or characterization evidence for risky boundaries. If proof is missing, leave the guard in place rather than asserting it is dead.

Classify candidates: `PROVEN_REDUNDANT` (safe to remove), `INDEPENDENT_BOUNDARY` (retain), or `UNPROVEN` (investigate or retain).

Reject findings based solely on line count, cosmetic preference, a theoretical future feature, an imagined failure, or a tool metric. Prefer subtraction before invention. Do not add a factory, adapter, fallback, hash, retry, cache, configuration, or extra file unless required by the current contract, observed failure, or real boundary.

### 4. Apply narrowly, when authorized

- Make one coherent simplification at a time; validate locally with the smallest relevant deterministic checks, expanding for affected cross-boundary behavior.
- Preserve supported input/output behavior and error taxonomy, contractual failure timing, side effects, ordering, concurrency semantics, and persistence effects. Only the proven unreachable, non-contractual exception in Step 3 is exempt.
- **Production-code refactoring is not a license to weaken tests merely to get green.** Explicit test-suite work may remove proven redundant tests without claiming their contract was invalid. Dropping *unique but low-value* detection is a distinct risk-budget decision: propose it first; implement only after specific approval consistent with repository testing policy. An actual product contract change needs its own authority.
- Do not trade understandable control flow for dense one-liners or over-inlining; keep helpers that name real concepts or isolate lifecycle/error boundaries.
- Do not replace genuine failures with broad `catch`, silent fallback, extra retries, timeout increases, weakened assertions, or implementation-detail mocks.
- Avoid unrelated cleanup. Record out-of-scope findings briefly instead of fixing them in the same diff.


## Test reduction and portfolio review (`focus tests` / `focus test-portfolio`)

Activate `tests` for evidence-backed removal of redundant tests/fixtures. Activate `test-portfolio` when the user asks whether **even correct, uniquely detecting tests** deserve permanent maintenance. These are different decisions: **redundant detection can be removed with equivalence evidence; unique detection can be dropped only by explicit risk acceptance**. A passing test is not inherently valuable, and line coverage is not a retention mandate. The goal is a smaller *necessary detection portfolio*, not a target deletion count.

### 1. Inventory and assign detection ownership

- Scope to the named suites, including relevant files unchanged by the PR. Inventory test files/scenarios, expensive fixtures, and overlapping unit/property/component/API/DB/E2E checks. Review bounded clusters by contract, input/state partition, failure mechanism, oracle, layer, and execution cost. State what was **not** examined; never generalize a sampled result to the whole suite.
- For each meaningful candidate, map `test → supported contract → state partition → plausible fault → oracle → detection layer/owner`. Review actual assertions and production call paths, not titles, comments, coverage numbers, or similarity scores.
- Identify the **minimum sufficient layer** for the fault. Pure domain behavior belongs near the domain; wire validation needs at least a wiring witness; SQL/transactions require real DB semantics; browser timing, navigation, session, and rendering mechanics need their real boundary when material. One authority does not erase independent enforcement points.

### 2. Challenge the reason to keep a test

Ask in order:
1. **Contract:** Is this an accepted/current requirement, an actual past regression, an independent boundary, or merely an implementation branch, speculative fallback, obsolete compatibility promise, or historical test name? An obsolete label alone does not prove the behavior is obsolete.
2. **Distinct fault:** What plausible defect can *this* test catch that retained tests cannot? Compare setup, state partition, act, oracle, environment, and timing; do not infer domination from similar code or narrower assert count alone.
3. **Impact:** Would failure cause security/authorization bypass, wrong state transition, lost/corrupted data, race, transaction violation, persistence drift, recovery failure, deployment failure, or material user harm? These typically require owned detection even when rare.
4. **Cost and placement:** Does a cheap, deterministic lower-layer test already own the logic? Is a slower integration/browser check justified by its unique composition? Does the fixture/setup create more cost than the assertion? Could parameterization or fixture consolidation remove cost without dropping detection?
5. **Maintenance value:** For *low-impact* unique detections, compare concrete maintenance/flakiness/runtime cost against likely defect detection and available upstream or broader checks. Do not pretend the detection is redundant just because it is low-value.

Apply by layer, not by universal test-count targets:
- **Unit:** Keep nontrivial transformations, state machines, decision partitions, and invariants; challenge getters, trivial forwarding/mapping, call-count mirrors, and repeated happy paths that prove only implementation.
- **Property-based:** Keep meaningful general laws, state-space/sequence invariants, and counterexamples not cheaply owned by examples; challenge generators with no actual breadth and redundant example assertions. Never require a new property-test framework merely to reduce tests.
- **Smoke:** Keep a small number of real composition/deployment/boot witnesses; challenge per-page/per-route success-only checks already owned by focused tests. A self-registered test route is not a production integration witness.
- **Component/API/DB/E2E:** Own the distinct wire, authorization, persistence, browser, or distributed mechanism. Avoid retaining the same deterministic business rule in every layer without an independently named failure mode.

### 3. Classify; do not disguise policy choices as equivalence

- `DELETE_REDUNDANT`: No **unique required** detection; identify the retained owner and show it detects the same defect/partition at a sufficient layer. Can apply with test-edit authorization.
- `CONSOLIDATE`: Merge cases/assertions or remove repeated fixture/setup while retaining every required input partition and oracle. Verify test ownership, isolation, cleanup, and concurrency before sharing state. Can apply with test-edit authorization.
- `DROP_OBSOLETE`: The behavior is demonstrably outside the **authoritative current** contract (removed or superseded). Show the contract/history evidence and assess whether the corresponding production fallback must also be removed. Do not silently change an accepted contract; product changes need separate authorization.
- `DROP_LOW_VALUE`: **There is unique detection, but retaining it may cost more than its low-impact fault risk.** Record exactly what will no longer be detected, affected boundary, maintenance/runtime cost, remaining partial signals, and risk owner. This is a **proposal, not an executable deletion** until the user specifically accepts that lost detection and repository policy permits it. Do not use for an unowned high-impact boundary.
- `KEEP_CRITICAL`: Required contract or distinct high-impact failure owner; keep even if a strict code-shape duplicate looks tempting. Tests at distinct independent boundaries may both be necessary.
- `UNPROVEN`: Contract, call graph, fault equivalence, or risk acceptance uncertain; retain pending evidence.

Classifications are about the **test asset**, not permission to weaken production behavior. Removing a non-contractual production guard and deleting its test is a separate code+test change with the Step 3 proof obligation. No unsupported state is "impossible" solely because of a TypeScript type. Do not silently drop rejection tests for public inputs, authz/tenant boundaries, time and concurrency protocols, transactions, or persistence integrity.

### 4. Apply, verify, and stop

- Apply `DELETE_REDUNDANT`/`CONSOLIDATE` incrementally when authorized. For `DROP_OBSOLETE`, first confirm contract authority; for `DROP_LOW_VALUE`, request **specific risk acceptance** separate from general edit permission. Otherwise leave the candidate unchanged and report it.
- Remove actual `it/test` cases, data rows, mock layers, and redundant fixture work; do not present turning off coverage instrumentation, renaming CI, using `skip`, broad mocks, retries, or weakened assertions as test simplification.
- Run targeted tests and proportionate cross-boundary gates. Where material, use an existing regression, deterministic negative test, or focused counterfactual to check detection ownership; no mandatory mutation campaign. Record before/after case counts, test/support-code change, comparable runtime, affected contract owners, and tests not run. Never claim the whole CI critical path improved from single-suite timing.
- **Stopping rule:** No deletion quota; stop when remaining candidates either own important faults, are not cost-effective to assess, or lack proof/authorization. For a suite-wide `NO_CHANGE`, show examined clusters and concrete comparisons; a CI-only change or superficial spot-check is not a full portfolio review.

**Review output:** For material candidates, show `file/test | contract + fault mechanism | classification | retained owner or explicit detection loss | evidence | action/approval needed`. Distinguish **safe subtraction**, **proposed risk-budget removal**, and **product-contract changes** in separate groups.

## Verification and stop rule

Choose checks based on impact: focused tests → affected package/static gates → PostgreSQL, E2E, or full verification **when warranted**. Do not claim PASS for tests not run. Never add mandatory CRAP scores, similarity thresholds, mutation campaigns, full-suite loops, or three-agent rituals to a routine small simplification. Those tools are optional for a demonstrated complexity or test-quality question.

Stop when the behavior is preserved and no remaining candidate has a credible cost/benefit case. **If nothing is worth changing, report `NO_CHANGE` and why.**

## Completion report

Keep it short, factual, and useful:

1. `SCOPE`: baseline/diff and focus; `MODE`: REVIEW or APPLY.
2. `CHANGED` (or `NO_CHANGE`): files and complexity removed; for deleted tests give detection ownership, and for portfolio review list proposals with explicit lost signal and any pending risk approval.
3. `PRESERVED`: invariants and independent boundaries intentionally retained.
4. `VERIFIED`: exact commands, results, and any skipped checks.
5. `REMAINING`: only concrete, material risks or deferred findings.
