---
name: jn-semantic
description: Extract research or system semantics from a technical problem, paper, benchmark, API, runtime, database mechanism, sandbox, storage system, or agent workflow. Short key for personal invocation.
---

# Semantic Extraction Skill

## Purpose

This skill helps transform a vague technical topic, feature-rich system, paper idea, benchmark, or engineering design into a clear semantic model.

The goal is to identify:

```text
operation × condition/state × object/context → observable behavior / guarantee / cost / violation
```

---

## Core Principle

A feature answers: "What can the system do?"
A semantic model answers: "Under what conditions, when this operation is applied to this object, what behavior is guaranteed, allowed, denied, persisted, rolled back, observed, or violated?"

A research gap appears when a claimed feature has hidden preconditions, a guarantee changes under different workloads, an operation has ambiguous behavior, a trade-off is not measured, or a semantic dimension is not captured by existing APIs/benchmarks.

---

## Required Output Style

Produce structured analysis in Chinese unless the user asks otherwise. Prefer these sections:

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

---

## The Six-Step Semantic Extraction Method

### Step 1: Identify First Principles

Ask: Why does this system/mechanism need to exist? What value does it provide that the simpler baseline does not? What would happen if we removed it?

Common first-principle forms:

| Domain | First-principle goal |
|---|---|
| Sandbox | 最小权限下保留最大任务能力 |
| Database index | 在更新成本与查询效率之间压缩搜索空间 |
| PMem | 在持久性语义与内存式访问之间做权衡 |
| Runtime | 把资源调度、并发、等待、错误恢复变成可控抽象 |
| IO API | 把阻塞/异步/backend 差异隐藏或显式化 |
| Benchmark | 隔离变量，测出机制对行为的影响 |

Convert generic words ("performance", "security") into observable questions.

**Completion criterion**: At least one specific first-principle question formulated that a simpler baseline does not address.

### Step 2: Identify Basic Operations

Find the smallest repeated actions. Operations should be verbs. If an operation hides many actions, split it.

Examples: read/write/execute for sandbox; point lookup/range scan for database; spawn/await/block for runtime.

**Completion criterion**: Operation list complete with at least 5 primitive verbs.

### Step 3: Identify Objects and Resources

The same operation has different meaning on different objects. Build a table: Operation | Object | Semantic meaning.

**Completion criterion**: At least 3 operation-object pairs with distinct semantic meanings.

### Step 4: Identify States, Stages, and Conditions

Semantic differences appear under state changes. Ask: When does the same operation become legal, illegal, expensive, unsafe, or meaningless?

**Completion criterion**: At least 2 state-dependent semantic differences identified.

### Step 5: Identify Observable Effects

Semantics must land on evidence. Ask: What can we observe from outside the mechanism?

If no observable effect can be defined, the semantic claim is probably too vague.

**Completion criterion**: Each identified operation has at least one measurable observable effect.

### Step 6: Define Rules, Guarantees, and Violations

A semantic model is not complete until it can say: allowed / denied / persisted / rolled back / ordered / visible / isolated / failed / retried.

**Completion criterion**: At least one rule of the form "If condition, then behavior" is defined.

---

## Semantic Classification Table

See `reference/CLASSIFICATION.md` for the full table of semantic types (capability, safety, persistence, ordering, isolation, performance, compatibility, observability, recovery, learning).

---

## Research Gap Patterns

See `reference/GAP-PATTERNS.md` for common patterns (feature exists but semantics unclear, API exists but guidance missing, strong claim depends on hidden substrate, benchmark measures outcome not mechanism, learning from traces, cross-backend equivalence).

---

## Output Templates

See `reference/OUTPUT-TEMPLATES.md` for short and full report templates.

---

## Quality Bar

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
- Uses vague words ("secure", "fast", "robust") without observable metrics.
- Does not distinguish object types.
- Ignores state/stage.
- Has no failure or violation cases.
- Cannot produce an experiment.

---

## Reference Files

| File | Content |
|---|---|
| `reference/CLASSIFICATION.md` | Semantic classification table |
| `reference/GAP-PATTERNS.md` | Research gap patterns + trade-off/sensitivity analysis |
| `reference/OUTPUT-TEMPLATES.md` | Short and full report templates |
