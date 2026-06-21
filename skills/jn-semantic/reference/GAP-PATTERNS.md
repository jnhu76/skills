# Research Gap Patterns

Look for these patterns:

## Pattern 1: Feature exists, semantics unclear

Example: "The system supports rollback. But what exactly rolls back? Files? Memory? Processes? Network effects? External API calls?"
Gap: rollback coverage semantics

## Pattern 2: API exists, programming guidance missing

Example: "PMem provides flush/fence APIs. But how should data structures be designed around persistence ordering?"
Gap: API semantics → programming model

## Pattern 3: Strong claim depends on hidden substrate

Example: "Fast sandbox startup depends on snapshot + CoW + filesystem reflink + warm pool."
Gap: runtime + storage co-design under agent workloads

## Pattern 4: Benchmark measures outcome, not mechanism

Example: "A benchmark shows range scan speed. But does not isolate cache locality, persistence ordering, write amplification, or recovery behavior."
Gap: mechanism-isolating benchmark design

## Pattern 5: Learning from traces can learn the wrong thing

Example: "An audit trace contains malicious postinstall behavior. Naive learner converts it into allowed policy."
Gap: poisoning-resistant policy learning

## Pattern 6: Same policy does not mean same behavior across backends

Example: "Deny network in Docker, bubblewrap, and microVM may differ in DNS, proxy, loopback, metadata IP, or IPv6 behavior."
Gap: cross-backend semantic equivalence

# Trade-off and Sensitivity Analysis

## Common Trade-offs

- strong isolation ↔ startup latency
- least privilege ↔ false deny
- snapshot rollback ↔ storage complexity
- trace detail ↔ overhead / privacy
- PMem persistence guarantee ↔ flush cost
- range scan speed ↔ update cost

## Sensitive Variables

Variables that change the conclusion: backend type, filesystem type, cache state, range size, model capability, policy strictness, network availability, workload shape, crash point, dependency behavior.

## Non-sensitive Variables

Implementation details that don't change core conclusions: renaming policy fields, JSON vs YAML, minor CLI wrapper changes, log formatting.

Do not confuse implementation variation with semantic variation.
