# CapGuard v0.3 Addendum: First-Principles Sandbox Boundary Layer

## New Positioning

CapGuard does not compete with microVM sandboxes at the hypervisor layer. It studies the agent-facing control layer above sandbox backends:

```text
Agent Intent → Policy Compiler → Sandbox Backend → OS-visible Effects → Trace Verifier → Capability/Safety Report
```

## New Research Questions

### RQ5: Backend Trade-off Surface

How do sandbox backends differ in security boundary, startup latency, runtime overhead, host dependency, and agent task compatibility?

### RQ6: Runtime + Storage Co-design

How do snapshot, writable-layer, cache, and filesystem choices affect agent workload latency, tail behavior, rollback capability, and disk amplification?

### RQ7: Effect and Rollback Semantics

Which effects are allowed, denied, logged, replayed, and rollbackable? Which effects are non-rollbackable, such as network requests, package registry side effects, external API calls, and remote telemetry?

### RQ8: Trace Verification

Can execution traces prove that observed effects matched the declared user intent and policy, without learning poisoned or unnecessary permissions?

## New Metrics

| Metric | Meaning |
|---|---|
| HDF: Host Dependency Factor | Number and severity of required host capabilities |
| RIS: Runtime Impact Score | Startup + runtime + I/O overhead under agent workload |
| RCS: Rollback Coverage Score | Fraction of effects covered by rollback semantics |
| TVR: Trace Verification Rate | Fraction of policy decisions explainable from trace evidence |
| ESI: External Side-effect Index | Count and severity of non-rollbackable external effects |

## Updated System View

```text
Threat Model
  ↓
WorkSpec / User Intent
  ↓
Policy Compiler
  ↓
Backend Adapter
  ├── Local audit wrapper
  ├── Docker/rootless Docker
  ├── bubblewrap/Sandlock-like backend
  ├── gVisor optional
  └── microVM/CubeSandbox optional baseline
  ↓
Effect Trace
  ↓
Trace Verifier + Poisoning Filter
  ↓
CPR / ASR / FDR / SBR / Tool Shift / PIR / RCS / TVR
```
