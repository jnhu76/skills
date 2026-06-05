---
name: jn_sandbox
description: Analyze AI agent sandbox systems, repositories, papers, and design docs to find first-principles R&D or research gaps. Use when reviewing sandbox projects such as microVM, Docker, gVisor, bubblewrap, Firecracker, E2B-compatible sandboxes, or when updating CapGuard research plans around security, least privilege, performance, isolation, deployability, policy synthesis, trace verification, and rollback semantics. Short key for personal invocation.
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
- update a CapGuard-style research plan;
- design experiments around least privilege, policy synthesis, trace verification, sandbox-induced behavior changes, or rollback semantics;
- convert a README claim into an evidence table or benchmark plan.

---

## Non-Goals

Do not turn the review into a feature checklist. Do not assume stronger isolation is always better. Do not assume README claims are false. Treat strong systems as baselines, not enemies.

Avoid claiming that a system is insecure unless there is evidence. Prefer wording like:

```text
This is a boundary or unverified assumption, not necessarily a vulnerability.
```

---

## First-Principles Review Frame

Always start with these questions:

1. **Why sandbox?**
   - What unsafe OS-visible effects are being reduced?
   - What secrets, files, sockets, devices, networks, processes, or host capabilities are protected?
   - Would a separate user account, rootless container, or local wrapper be enough?

2. **What capability must be preserved?**
   - Can the agent still search, read, edit, build, test, install dependencies, run browsers, use caches, and export diffs?
   - Does the policy cause false denies, retry explosions, tool shift, or dangerous workarounds?

3. **What isolation boundary is actually provided?**
   - Process/user boundary?
   - Namespace/cgroup boundary?
   - User-space kernel boundary?
   - Guest kernel / microVM boundary?
   - Hardware virtualization boundary?

4. **What performance is being optimized?**
   - Cold start latency?
   - Warm start latency?
   - Snapshot restore time?
   - Runtime overhead?
   - File-system overhead?
   - Network overhead?
   - High-concurrency tail latency?

5. **What host assumptions are required?**
   - KVM, nested virtualization, PVM, root privileges, eBPF, XFS reflink, cgroup version, kernel version, device passthrough, special cloud environment, privileged daemon, or storage layout.

6. **What is the semantic effect model?**
   - Which effects are allowed, denied, logged, replayed, rolled back, or impossible to roll back?
   - Are external effects such as HTTP requests, package downloads, postinstall scripts, telemetry, or remote API calls modeled?

---

## Required Output Structure

When reviewing a sandbox system, produce the following sections.

### 1. One-Sentence Positioning

State what the system really is. Example:

```text
This is not merely a container runtime; it is a microVM-backed sandbox control plane optimized for fast agent execution under stronger-than-container kernel isolation.
```

### 2. Claim Table

Create a table:

| Claim | Evidence in README/code/docs | Hidden Assumption | Boundary / Failure Mode | Experiment |
|---|---|---|---|---|

For every strong claim, identify what must be true for the claim to hold.

### 3. Trade-off Map

Classify each design point:

| Design Point | Benefit | Cost | Type |
|---|---|---|---|

Use these categories:

- **Trade-off**: improves one property while worsening another.
- **Sensitive point**: small environmental change may strongly affect results.
- **Risk point**: can cause correctness, security, or operability failure.
- **Non-sensitive point**: unlikely to affect the core claim.
- **Unknown**: insufficient evidence; requires experiment.

### 4. First-Principles Baseline Check

Compare against simpler baselines:

| Baseline | What it protects | What it fails to protect | Why stronger sandbox may be justified |
|---|---|---|---|
| Separate OS user | | | |
| Rootless container | | | |
| Docker | | | |
| bubblewrap / namespace wrapper | | | |
| gVisor | | | |
| microVM / KVM | | | |

### 5. Research Gap Candidates

Do not propose vague gaps. Each gap must have:

```text
Observation → Missing knowledge → Single variable → Metric → Expected contribution
```

Example:

```text
Observation: Fast startup depends on snapshot and copy-on-write storage.
Missing knowledge: We do not know how startup latency degrades across storage backends under agent workloads.
Single variable: filesystem/snapshot backend.
Metric: create latency, P95/P99, runtime overhead, task success, disk amplification.
Contribution: a workload-grounded model of runtime + storage co-design for agent sandboxes.
```

### 6. Safety Semantics Review

Analyze:

- file read/write policy;
- network egress policy;
- secret exposure;
- package install and postinstall;
- shell escape surface;
- host mount and socket exposure;
- device/GPU exposure;
- rollback limitations;
- trace trustworthiness;
- policy learning poisoning risk.

### 7. Experiment Plan

Prefer small, falsifiable experiments:

| RQ | Hypothesis | Variable | Controls | Metrics | Minimal Setup |
|---|---|---|---|---|---|

The experiment should be able to disprove the claim, not just demonstrate success.

---

## CapGuard Research Update Rules

When updating a CapGuard-style research plan, preserve the core v0.2 contribution if it already focuses on:

- sandbox-induced capability degradation;
- tool preference shift;
- intent-aware privilege projection;
- poisoning-resistant policy learning;
- CPR / ASR / SBR / FDR / Tool Shift / PIR metrics.

Then add a new first-principles layer above it:

```text
Sandbox purpose:
  safety = reduce dangerous OS-visible effects
  capability = preserve legitimate task completion
  performance = minimize startup and runtime overhead
  isolation = choose the right boundary for the threat model
  semantics = define allowed, denied, logged, replayed, and rollbackable effects
```

Add these new research questions when relevant:

- RQ5: How do different isolation backends change security, latency, compatibility, and host dependency trade-offs?
- RQ6: How do runtime + storage co-design choices affect agent workload latency, tail behavior, and rollback capability?
- RQ7: What is the formal or operational semantics of sandbox effects, including rollbackable and non-rollbackable effects?
- RQ8: Can traces prove that policy decisions matched user intent and did not allow unnecessary dangerous effects?

---

## Red Flags in a Sandbox README

Treat the following as review triggers:

- strong performance claim without workload definition;
- cold start number without P95/P99 or concurrency;
- “secure” without threat model;
- “isolated” without specifying kernel/user/VM boundary;
- “drop-in compatible” without API coverage matrix;
- “snapshot/rollback” without defining file, memory, process, network, and external side effects;
- “allow/deny network” without DNS, IPv6, proxy, metadata IP, and private network semantics;
- “policy learning” that treats first-run trace as ground truth;
- “least privilege” without false-deny and capability-preservation metrics.

---

## Final Answer Style

Be direct. If the existing project is strong, say so. Then identify the layer it does not address.

Use this pattern:

```text
Do not compete with this system at its strongest layer. Use it as a baseline. Move the research question one layer up or one layer sideways.
```

For example:

```text
Do not build another microVM runtime. Build the agent-facing policy compiler, effect semantics, trace verifier, and benchmark harness that can evaluate microVM, container, and local-wrapper backends under the same task and policy model.
```
