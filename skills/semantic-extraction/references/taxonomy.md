# Semantic Extraction Taxonomy

## 1. Core Formula

```text
Semantic = operation × object × state/condition → observable behavior / guarantee / violation / cost
```

## 2. Operation Types

| Domain | Operations |
|---|---|
| Sandbox / Agent | read, write, execute, network, inspect, install, test, patch, rollback, learn, verify |
| Database | lookup, range scan, insert, update, delete, compact, checkpoint, recover |
| Storage / PMem | load, store, flush, fence, persist, recover, log, scan |
| Runtime | spawn, schedule, block, poll, wake, cancel, timeout, retry |
| Network | connect, listen, resolve, send, receive, retry, proxy |
| API / Framework | create, configure, call, observe, extend, compose, fail, recover |

## 3. Object Types

| Domain | Objects |
|---|---|
| Sandbox | repo, tmp, cache, home, secret, docker.sock, registry, internet, metadata IP |
| DB | table, index, page, tuple, key range, WAL, memtable, SSTable |
| PMem | cache line, persistent region, log entry, pointer, object graph |
| Runtime | task, thread, event loop, queue, timer, cancellation token |
| Network | DNS, IP, socket, proxy, loopback, remote API |

## 4. State / Condition Types

| Type | Examples |
|---|---|
| Lifecycle | create, running, paused, resumed, killed, recovered |
| Execution stage | search, install, test, patch, summarize, cleanup |
| Cache state | cold, warm, dirty, flushed |
| Failure state | timeout, crash, partial write, denied, retry |
| Policy state | audit-only, static strict, reactive, intent-aware |
| Workload shape | small files, large scan, random access, sequential access |

## 5. Observable Effects

| Effect | Examples |
|---|---|
| File effect | read path, write path, delete path, chmod |
| Process effect | spawn, fork, exec, kill, daemon |
| Network effect | DNS query, TCP connect, HTTP POST, registry access |
| Storage effect | flush count, dirty bytes, write amplification |
| Recovery effect | rollback success, partial restore, stale state |
| Security effect | secret read, exfiltration, privilege escalation |
| Performance effect | P50/P95/P99, throughput, CPU, memory, I/O |

## 6. Semantic Types

| Type | Key question |
|---|---|
| Capability | What useful ability is preserved? |
| Safety | What dangerous effect is blocked? |
| Persistence | What survives crash or rollback? |
| Ordering | What must happen before what? |
| Isolation | What cannot affect what? |
| Performance | What cost appears under which workload? |
| Compatibility | What external behavior stays equivalent? |
| Recovery | What happens after failure? |
| Observability | What evidence can prove behavior? |
| Learning | What can be safely learned from traces? |
