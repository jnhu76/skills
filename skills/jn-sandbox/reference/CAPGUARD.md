# CapGuard Research Update

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

# Red Flags in a Sandbox README

Treat the following as review triggers:

- strong performance claim without workload definition;
- cold start number without P95/P99 or concurrency;
- "secure" without threat model;
- "isolated" without specifying kernel/user/VM boundary;
- "drop-in compatible" without API coverage matrix;
- "snapshot/rollback" without defining file, memory, process, network, and external side effects;
- "allow/deny network" without DNS, IPv6, proxy, metadata IP, and private network semantics;
- "policy learning" that treats first-run trace as ground truth;
- "least privilege" without false-deny and capability-preservation metrics.

# Final Answer Style

Be direct. If the existing project is strong, say so. Then identify the layer it does not address.

Use this pattern:

```text
Do not compete with this system at its strongest layer. Use it as a baseline. Move the research question one layer up or one layer sideways.
```

For example:

```text
Do not build another microVM runtime. Build the agent-facing policy compiler, effect semantics, trace verifier, and benchmark harness that can evaluate microVM, container, and local-wrapper backends under the same task and policy model.
```
