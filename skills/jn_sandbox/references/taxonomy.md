# Sandbox Gap Taxonomy

## Core Axes

| Axis | Question | Common Metrics |
|---|---|---|
| Safety | What dangerous effects are blocked? | SBR, secret exposure, network exfiltration, policy violations |
| Capability | What legitimate task ability is preserved? | CPR, task success, false deny rate, recovery cost |
| Isolation | What boundary separates guest from host? | kernel sharing, syscall mediation, VM boundary, attack surface |
| Performance | What overhead is introduced? | cold start, warm start, P95/P99, runtime overhead, I/O overhead |
| Deployability | What host assumptions are required? | KVM, root, eBPF, cgroups, filesystem, cloud support |
| Semantics | What effects are allowed, denied, logged, replayed, or rolled back? | trace completeness, rollback coverage, external side-effect leakage |
| Observability | Can we prove what happened? | audit coverage, trace fidelity, replayability, diff completeness |
| Policy Synthesis | Can permissions be predicted from intent? | precision, recall, over-permission, false deny avoidance |

## Backend Classes

| Backend | Strength | Weakness |
|---|---|---|
| Separate user | Simple, cheap | weak isolation, poor effect control |
| Local wrapper | easy tracing and iteration | weak enforcement unless backed by OS controls |
| Docker/rootless Docker | common, reproducible | shared kernel, daemon/socket risk, semantic gaps |
| bubblewrap/namespaces | lightweight least privilege | not full kernel isolation, policy complexity |
| gVisor | stronger syscall mediation | compatibility/runtime overhead |
| Firecracker/KVM microVM | strong kernel isolation | host dependency, image/storage complexity, orchestration cost |
| PVM/cloud microVM | strong isolation in constrained cloud | kernel/cloud-specific assumptions |

## Gap Types

- Measurement gap: no workload-grounded data.
- Semantic gap: policy terms do not define real OS effects.
- Verification gap: trace cannot prove enforcement correctness.
- Deployment gap: result depends on host features not surfaced in claims.
- Workload gap: benchmark does not match real agent tasks.
- Learning gap: trace-based policy learner may learn poisoned behavior.
- Lifecycle gap: pause/resume/snapshot/delete can race under concurrency.
