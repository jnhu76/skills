---
name: jn-sandbox
description: Analyze AI agent sandbox systems from first principles to find R&D gaps.
origin: hoooo.org
disable-model-invocation: true
license: MIT
metadata:
  version: "0.1.0"
  author: "CapGuard research workflow"
---

# Sandbox Gap Finder

## Purpose

Use this skill to review an AI agent sandbox system from first principles and identify credible R&D or research gaps. The goal is not to list features or praise architecture. The goal is to decompose claims into assumptions, trade-offs, sensitive points, measurable variables, and testable research questions.

The core lens is:

```text
minimum necessary privilege + maximum task capability + bounded execution effects + acceptable latency and overhead
```

A sandbox is useful only if it improves safety or controllability without destroying the agent's ability to complete legitimate work. If a sandbox does not improve safety, traceability, or controllability, compare it against simpler baselines such as running as a separate OS user, rootless containers, or a restricted wrapper.

---

## When to Use

Use this skill when the user asks to:

- review an agent sandbox repository, paper, or architecture;
- compare Docker, rootless Docker, bubblewrap, gVisor, Firecracker, KVM, microVM, E2B-like systems, or local wrappers;
- find research gaps or engineering gaps in a strong existing project;
- update a CapGuard-style research plan (see `reference/CAPGUARD.md`);
- design experiments around least privilege, policy synthesis, trace verification, sandbox-induced behavior changes, or rollback semantics;
- convert a README claim into an evidence table or benchmark plan.

---

## Non-Goals

Do not turn the review into a feature checklist. Do not assume stronger isolation is always better. Do not assume README claims are false. Treat strong systems as baselines, not enemies.

Avoid claiming that a system is insecure unless there is evidence.

---

## First-Principles Review Frame

Always start with these questions:

1. **Why sandbox?** What unsafe OS-visible effects are being reduced? What is protected? Would a separate user account or rootless container be enough?

2. **What capability must be preserved?** Can the agent still search, read, edit, build, test, install dependencies? Does the policy cause false denies or dangerous workarounds?

3. **What isolation boundary is actually provided?** Process/user? Namespace? User-space kernel? Guest kernel/microVM? Hardware virtualization?

4. **What performance is being optimized?** Cold/warm start? Snapshot restore? Runtime overhead? Filesystem/network? Tail latency?

5. **What host assumptions are required?** KVM, nested virtualization, root privileges, eBPF, kernel version, device passthrough, privileged daemon?

6. **What is the semantic effect model?** Which effects are allowed, denied, logged, replayed, rolled back? Are external effects like HTTP requests, package downloads, postinstall scripts modeled?

---

## Required Output Structure

### 1. One-Sentence Positioning

State what the system really is.

### 2. Claim Table

| Claim | Evidence in README/code/docs | Hidden Assumption | Boundary / Failure Mode | Experiment |
|---|---|---|---|---|

For every strong claim, identify what must be true for it to hold.

### 3. Trade-off Map

| Design Point | Benefit | Cost | Type |
|---|---|---|---|

Types: Trade-off / Sensitive point / Risk point / Non-sensitive point / Unknown.

### 4. First-Principles Baseline Check

Compare against simpler baselines: separate OS user, rootless container, Docker, bubblewrap, gVisor, microVM/KVM.

### 5. Research Gap Candidates

Each gap must have: Observation → Missing knowledge → Single variable → Metric → Expected contribution.

### 6. Safety Semantics Review

Analyze: file/network policy, secret exposure, package install, shell escape, host mount, rollback limitations, trace trustworthiness, policy learning poisoning risk.

### 7. Experiment Plan

| RQ | Hypothesis | Variable | Controls | Metrics | Minimal Setup |
|---|---|---|---|---|---|

The experiment should be able to disprove the claim, not just demonstrate success.

---

## Reference Files

| File | Content |
|---|---|
| `reference/CAPGUARD.md` | CapGuard research update rules, README red flags, final answer style |
