---
name: jn_semantic
description: Use this skill when you need to extract research or system semantics from a technical problem, paper, benchmark, API, runtime, database mechanism, sandbox, storage system, or agent workflow. It helps convert feature piles into operations, objects, states, observable effects, rules, invariants, trade-offs, research questions, and experiments. Short key for personal invocation.
---

# Semantic Extraction Skill

## Purpose

This skill helps transform a vague technical topic, feature-rich system, paper idea, benchmark, or engineering design into a clear semantic model.

Use it when the user says or implies:

- “这个问题怎么抽象？”
- “这个系统的语义是什么？”
- “怎么从一堆功能里找到论文点？”
- “这个 benchmark 为什么能写论文？”
- “这个 API / runtime / sandbox / database mechanism 的能力边界是什么？”
- “怎么找到研发缝隙 / 科研缝隙？”
- “怎么把第一性问题变成可实验变量？”

The goal is not to praise the system, summarize features, or produce generic architecture prose.

The goal is to identify:

```text
operation × condition/state × object/context → observable behavior / guarantee / cost / violation
```

This is the core definition of semantics used by this skill.

---

# Core Principle

A feature answers:

```text
What can the system do?
```

A semantic model answers:

```text
Under what conditions, when this operation is applied to this object, what behavior is guaranteed, allowed, denied, persisted, rolled back, observed, or violated?
```

A research gap appears when:

```text
a claimed feature has hidden preconditions,
a guarantee changes under different workloads,
an operation has ambiguous behavior,
a trade-off is not measured,
or a semantic dimension is not captured by existing APIs/benchmarks.
```

---

# Required Output Style

When using this skill, produce structured analysis in Chinese unless the user asks otherwise.

Prefer these sections:

1. 第一性目标
2. 基本操作
3. 操作对象
4. 状态 / 阶段 / 条件
5. 可观察效果
6. 语义分类
7. 规则 / 不变量 / 保证
8. 权衡面
9. 敏感变量与非敏感变量
10. 科研缝隙 / 研发缝隙
11. 可执行实验
12. 最小结论

Keep the answer direct. Do not over-polish. Do not turn it into marketing copy.

---

# The Six-Step Semantic Extraction Method

## Step 1: Identify First Principles

Ask:

```text
Why does this system/mechanism need to exist?
What value does it provide that the simpler baseline does not?
What would happen if we removed it?
```

Common first-principle forms:

| Domain | First-principle goal |
|---|---|
| Sandbox | 最小权限下保留最大任务能力 |
| Database index | 在更新成本与查询效率之间压缩搜索空间 |
| PMem | 在持久性语义与内存式访问之间做程序设计权衡 |
| Runtime | 把资源调度、并发、等待、错误恢复变成可控抽象 |
| IO API | 把阻塞/异步/backend 差异隐藏或显式化 |
| Benchmark | 隔离变量，测出机制对行为的影响 |

Avoid stopping at generic words such as “performance”, “security”, “scalability”, or “compatibility”. Convert them into observable questions.

Example:

```text
Bad:
这个 sandbox 更安全。

Good:
这个 sandbox 是否阻止 agent 读取 secret、外发网络请求、写出 workspace，并在阻断后仍保留运行测试和修改 repo 的能力？
```

---

## Step 2: Identify Basic Operations

Find the smallest repeated actions.

Examples:

### Sandbox / Agent

```text
read, write, execute, network, inspect, install, test, patch, rollback, learn, verify
```

### Database / Storage

```text
point lookup, range scan, insert, update, delete, flush, persist, recover, compact
```

### Runtime / IO

```text
spawn, await, block, schedule, cancel, poll, wake, retry, timeout
```

### API / Framework

```text
create, configure, call, observe, fail, recover, compose, extend
```

Rules:

- Operations should be verbs.
- Do not use feature names as operations unless they describe a primitive action.
- If an operation hides many actions, split it.

---

## Step 3: Identify Objects and Resources

The same operation has different meaning on different objects.

Example for sandbox:

| Operation | Object | Semantic meaning |
|---|---|---|
| read | repo source | usually legitimate |
| read | `.env` | secret exposure risk |
| read | `~/.ssh/id_rsa` | default deny |
| write | repo file | patch capability |
| write | `/etc/hosts` | system mutation |
| network | package registry | install-stage capability |
| network | unknown endpoint | exfiltration risk |
| access | docker.sock | host-control capability |

Example for PMem:

| Operation | Object | Semantic meaning |
|---|---|---|
| write | cache line | volatile until flushed |
| flush | cache line | persistence boundary |
| scan | contiguous range | bandwidth-sensitive |
| scan | pointer-linked nodes | cache-miss sensitive |
| recover | log entry | crash-consistency guarantee |

---

## Step 4: Identify States, Stages, and Conditions

Semantic differences often appear only under state changes.

Ask:

```text
When does the same operation become legal, illegal, expensive, unsafe, or meaningless?
```

Examples:

### Sandbox stages

```text
search → install → test → patch → summarize → cleanup
```

Network access to `pypi.org` may be legal during `install`, suspicious during `test`, and illegal during `summarize`.

### Database states

```text
cold cache → warm cache
clean page → dirty page
before flush → after flush
before crash → after recovery
small range → large range
read-only workload → mixed workload
```

### Runtime states

```text
ready → running → blocked → cancelled → timed out → recovered
```

---

## Step 5: Identify Observable Effects

Semantics must land on evidence.

Ask:

```text
What can we observe from outside the mechanism?
```

Examples:

### Sandbox effects

```text
files_read
files_written
processes_spawned
network_connect
env_access
permission_denied
state_diff
rollback_result
external_side_effect
```

### Database effects

```text
latency
throughput
cache_miss
write_amplification
flush_count
recovery_time
stale_read
scan_bandwidth
tail_latency
```

### Runtime effects

```text
wakeups
context switches
queue length
cancellation latency
timeout behavior
scheduler fairness
resource leak
```

If no observable effect can be defined, the “semantic” claim is probably too vague.

---

## Step 6: Define Rules, Guarantees, and Violations

A semantic model is not complete until it can say:

```text
allowed / denied / persisted / rolled back / ordered / visible / isolated / failed / retried
```

Examples:

### Sandbox rule

```text
If stage == test
and effect == network_connect(any)
then deny or escalate,
unless policy explicitly declares networked integration tests.
```

### PMem rule

```text
If write is not followed by required flush/fence sequence,
then the value must not be assumed persistent after crash.
```

### Runtime rule

```text
If a task is cancelled,
then no later user-visible callback should commit state unless cancellation was explicitly masked.
```

---

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

---

# Trade-off and Sensitivity Analysis

After extracting semantics, identify:

## Trade-offs

A trade-off exists when improving one property predictably harms or constrains another.

Examples:

```text
strong isolation ↔ startup latency
least privilege ↔ false deny
snapshot rollback ↔ storage complexity
trace detail ↔ overhead / privacy
PMem persistence guarantee ↔ flush cost
range scan speed ↔ update cost
```

## Sensitive variables

A sensitive variable changes the conclusion.

Examples:

```text
backend type
filesystem type
cache state
range size
model capability
policy strictness
network availability
workload shape
crash point
dependency behavior
```

## Non-sensitive variables

A non-sensitive variable changes implementation details but not the core conclusion.

Example:

```text
renaming a policy field
using JSON instead of YAML
minor CLI wrapper changes
log formatting
```

Do not confuse implementation variation with semantic variation.

---

# Research Gap Patterns

Look for these patterns:

## Pattern 1: Feature exists, semantics unclear

Example:

```text
The system supports rollback.
But what exactly rolls back?
Files? Memory? Processes? Network effects? External API calls?
```

Research gap:

```text
rollback coverage semantics
```

## Pattern 2: API exists, programming guidance missing

Example:

```text
PMem provides flush/fence APIs.
But how should data structures be designed around persistence ordering?
```

Research gap:

```text
API semantics → programming model
```

## Pattern 3: Strong claim depends on hidden substrate

Example:

```text
Fast sandbox startup depends on snapshot + CoW + filesystem reflink + warm pool.
```

Research gap:

```text
runtime + storage co-design under agent workloads
```

## Pattern 4: Benchmark measures outcome, not mechanism

Example:

```text
A benchmark shows range scan speed.
But does not isolate cache locality, persistence ordering, write amplification, or recovery behavior.
```

Research gap:

```text
mechanism-isolating benchmark design
```

## Pattern 5: Learning from traces can learn the wrong thing

Example:

```text
An audit trace contains malicious postinstall behavior.
Naive learner converts it into allowed policy.
```

Research gap:

```text
poisoning-resistant policy learning
```

## Pattern 6: Same policy does not mean same behavior across backends

Example:

```text
Deny network in Docker, bubblewrap, and microVM may differ in DNS, proxy, loopback, metadata IP, or IPv6 behavior.
```

Research gap:

```text
cross-backend semantic equivalence
```

---

# Output Templates

## Short Template

```markdown
## 1. 第一性目标

这个问题的根本目标是：...

## 2. 基本操作

| 操作 | 含义 |
|---|---|

## 3. 对象 / 条件 / 状态

| 维度 | 取值 | 为什么重要 |
|---|---|---|

## 4. 可观察效果

| Effect | 证据 |
|---|---|

## 5. 语义规则

| 条件 | 操作 | 结果 |
|---|---|---|

## 6. 权衡与敏感变量

| 类型 | 内容 |
|---|---|

## 7. 科研 / 研发缝隙

1. ...
2. ...
3. ...

## 8. 最小实验

| 实验 | 控制变量 | 观察指标 |
|---|---|---|
```

## Full Template

Use `templates/jn_semantic-report.md`.

---

# Quality Bar

A good semantic extraction should:

- Distinguish feature from semantic guarantee.
- Identify operations, objects, states, and effects.
- Produce at least one rule of the form `condition → behavior`.
- Identify hidden assumptions and substrate dependencies.
- Separate safety, performance, compatibility, and recovery semantics.
- Produce testable research or engineering gaps.
- Suggest experiments with controlled variables.

A weak semantic extraction usually:

- Lists features only.
- Uses vague words like “secure”, “fast”, “robust” without observable metrics.
- Does not distinguish object types.
- Ignores state/stage.
- Has no failure or violation cases.
- Cannot produce an experiment.

---

# Final Reminder

Do not ask “what features does it have?”

Ask:

```text
When this operation touches this object under this condition,
what is guaranteed,
what is observable,
what can fail,
what is the cost,
and what rule should guide program design?
```
