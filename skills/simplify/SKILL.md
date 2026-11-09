---
name: simplify
description: >
  Evidence-grounded simplification of working code. Use after a feature or bug fix,
  during PR review, or when asked to simplify, reduce overengineering, remove
  redundant defenses, reuse existing implementations, or improve clarity without
  changing behavior. Defaults to the current diff; preserves contracts and
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

**One authority is not one enforcement point.** A shared authorization rule may be implemented once and still require enforcement at several independent entrypoints. The same is true for authentication, state transitions, transactions, persistence constraints, and time/concurrency protocols.

### 2. Find candidates in three dimensions

- **Reuse:** Same responsibility implemented more than once; duplicate adapters, DTOs, helpers, error mappings, or existing library functionality rewritten locally. Prefer a single semantic owner, without creating an all-purpose abstraction.
- **Clarity:** Speculative extension points, wrapper chains, unnecessary indirection, nested control flow, confusing names, redundant comments, stale compatibility code past its documented retirement, or defensive code without a supported failure model.
- **Efficiency:** Demonstrably redundant database queries, allocations, rendering, I/O, or repeated work. Do not call a rewrite an optimization without relevant measurements or a clear cost model.

Use one reviewer by default. Parallel independent reviews are optional only for large, genuinely separable diffs; consolidate and deduplicate before changes.

### 3. Gate each proposed subtraction

Keep a candidate only when all are true:
1. The underlying responsibility and contract are understood.
2. Its complexity cost is material (comprehension, maintenance, correctness, or measured runtime).
3. The simpler alternative preserves all externally observable behavior, or a changed contract has been explicitly authorized.
4. The change is small, cohesive, and within task scope.
5. There is an independent, proportionate verification signal.

Reject findings based solely on line count, cosmetic preference, a theoretical future feature, an imagined failure, or a tool metric. Prefer subtraction before invention. Do not add a factory, adapter, fallback, hash, retry, cache, configuration, or extra file unless required by the current contract, observed failure, or real boundary.

### 4. Apply narrowly, when authorized

- Make one coherent simplification at a time; validate locally with the smallest relevant deterministic checks, expanding for affected cross-boundary behavior.
- Preserve inputs, outputs, error taxonomy, failure timing where contractual, side effects, ordering, concurrency semantics, and persistence effects.
- Refactoring is not a reason to edit tests until they pass. Existing tests should continue to pass. If a test itself asserts an invalid contract, prove that separately and seek authorization for the contract change.
- Do not trade understandable control flow for dense one-liners or over-inlining; keep helpers that name real concepts or isolate lifecycle/error boundaries.
- Do not replace genuine failures with broad `catch`, silent fallback, extra retries, timeout increases, weakened assertions, or implementation-detail mocks.
- Avoid unrelated cleanup. Record out-of-scope findings briefly instead of fixing them in the same diff.

## Exam-specific safeguards

When working in `jnhu76/exam`:

- Read the relevant rules in `AGENTS.md`, `docs/standards/code-quality.md`, and `docs/standards/testing.md` as needed, plus the owning architecture/contract or Accepted ADR for affected behavior.
- Keep authoritative domain transitions in the engine/command layer, data access in repositories, and contract types/schemas in their owning packages. Never turn this skill into an excuse to bypass type safety, authorization, server-time authority, snapshot semantics, versioned answer saving, idempotency, or PostgreSQL transaction guarantees.
- Treat server/client and route/repository boundaries, or two independent public entrypoints, as separate trust boundaries until proven otherwise.
- Verify SQL semantics with real PostgreSQL where changed; browser-visible behavior with browser evidence; state/race behavior with controlled clocks or barriers. Do not replace these with mocks or sleeps.
- Keep local/CI test suites and deployment checks unless CI policy is being explicitly changed in a separate, reviewable task. Coverage percentage alone is neither a reason to add claim-free tests nor a reason to delete contract tests.

## Verification and stop rule

Choose checks based on impact: focused tests → affected package/static gates → PostgreSQL, E2E, or full verification **when warranted**. Do not claim PASS for tests not run. Never add mandatory CRAP scores, similarity thresholds, mutation campaigns, full-suite loops, or three-agent rituals to a routine small simplification. Those tools are optional for a demonstrated complexity or test-quality question.

Stop when the behavior is preserved and no remaining candidate has a credible cost/benefit case. **If nothing is worth changing, report `NO_CHANGE` and why.**

## Completion report

Keep it short, factual, and useful:

1. `SCOPE`: baseline/diff and focus; `MODE`: REVIEW or APPLY.
2. `CHANGED` (or `NO_CHANGE`): files and the specific complexity removed.
3. `PRESERVED`: invariants and independent boundaries intentionally retained.
4. `VERIFIED`: exact commands, results, and any skipped checks.
5. `REMAINING`: only concrete, material risks or deferred findings.

## Reference principles

- Claude `/simplify`: diff-scoped reuse, quality, efficiency review; optional parallelism.
- Addy Osmani `code-simplification`: comprehend first, preserve behavior, stay local, prefer clarity over compactness.
- `avoid-overkill`: evidence gate for speculative guards, fallbacks, retries, abstractions, and scope creep.
- Uncle Bob `ub-mode`: make it work, then make it right; subtract before adding; model boundaries; test behavior rather than implementation.

These are sources of ideas, not mandatory external dependencies or overriding instructions.
