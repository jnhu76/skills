---
name: simplify
description: >
  Evidence-grounded simplification of working code. Use after a feature or bug fix,
  during PR review, or when asked to simplify, reduce overengineering, remove
  redundant defenses, reuse existing implementations, or improve clarity without
  changing supported contract behavior. Defaults to the current diff; preserves contracts and
  independent security, concurrency, transaction, and persistence boundaries.
---

# Simplify — Evidence-Grounded Code Reduction

**Goal:** Make correct code easier to understand and maintain, with the smallest coherent change. Optimize for fewer concepts and lower lifetime cost, not fewer lines. **No change is a valid result.**

## Authority and execution mode

1. Read the repository's agent instructions first (`AGENTS.md`; `CLAUDE.md` may be a thin adapter). Follow the relevant Accepted ADR, domain contracts, and testing policy. This skill never overrides them.
2. Determine authorization: **review** is read-only; **apply** requires explicit permission to modify files. Do not commit, push, merge, or change protected resources unless separately authorized by the repository's rules.
3. Scope defaults to the current task or PR diff. For a PR, compare the correct merge base against the PR head; include staged and unstaged changes. Do not mistake `git diff HEAD` for the full PR diff. If there is no clear diff, request or identify a bounded target. Protect unrelated worktree changes.
4. Optional focus: `reuse`, `clarity`, `defenses`, `tests`, `efficiency`, or a named function/module. Focus changes review priority, never the safety bar.

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
- **Efficiency:** Observably redundant queries, allocations, rendering, I/O, or repeated work. Require measurement or a clear cost model before claiming a performance gain.

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
- Refactoring is not a reason to edit tests until they pass. Existing tests should continue to pass. If a test itself asserts an invalid contract, prove that separately and seek authorization for the contract change.
- Do not trade understandable control flow for dense one-liners or over-inlining; keep helpers that name real concepts or isolate lifecycle/error boundaries.
- Do not replace genuine failures with broad `catch`, silent fallback, extra retries, timeout increases, weakened assertions, or implementation-detail mocks.
- Avoid unrelated cleanup. Record out-of-scope findings briefly instead of fixing them in the same diff.



## Verification and stop rule

Choose checks based on impact: focused tests → affected package/static gates → PostgreSQL, E2E, or full verification **when warranted**. Do not claim PASS for tests not run. Never add mandatory CRAP scores, similarity thresholds, mutation campaigns, full-suite loops, or three-agent rituals to a routine small simplification. Those tools are optional for a demonstrated complexity or test-quality question.

Stop when the behavior is preserved and no remaining candidate has a credible cost/benefit case. **If nothing is worth changing, report `NO_CHANGE` and why.**

## Completion report

Keep it short, factual, and useful:

1. `SCOPE`: baseline/diff and focus; `MODE`: REVIEW or APPLY.
2. `CHANGED` (or `NO_CHANGE`): files, complexity removed, and proof for any deleted defense.
3. `PRESERVED`: invariants and independent boundaries intentionally retained.
4. `VERIFIED`: exact commands, results, and any skipped checks.
5. `REMAINING`: only concrete, material risks or deferred findings.
