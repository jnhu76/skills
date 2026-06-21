# Semantic Classification Table

Use this table to classify extracted semantics.

| Type | Meaning | Example |
|---|---|---|
| Capability semantic | What ability is preserved? | run tests, scan range, perform async IO |
| Safety semantic | What unsafe behavior is blocked? | deny secret read, prevent stale recovery |
| Persistence semantic | What survives crash/restart/rollback? | flushed PMem write, checkpointed file |
| Ordering semantic | What must happen before what? | flush before publish, deny before execute |
| Isolation semantic | What cannot influence what? | guest kernel isolated from host kernel |
| Performance semantic | What cost changes under workload? | scan latency, startup overhead, syscall cost |
| Compatibility semantic | What existing API behavior is preserved? | E2B-compatible API, POSIX-like semantics |
| Observability semantic | What evidence can be collected? | trace, audit log, effect diff |
| Recovery semantic | What happens after failure? | rollback, retry, crash recovery |
| Learning semantic | What can be learned from trace? | stable allowlist vs poisoned behavior |
