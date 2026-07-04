# C++ Lock-Free

无锁 C++ 和高级原子内存序算法的专家领域。

## 用途

设计、实现、审计、推理显式无锁 C++ 和高级 atomic/memory-order 算法。

## 核心关注

不是 "更快的 mutex"，是独立的正确性领域。

- **线性化点** — 每个操作的逻辑生效时刻
- **内存序推理** — acquire/release/relaxed/fence 的正确证明
- **ABA 问题** — 指针/索引 reuse 的分析
- **内存回收** — hazard pointer、epoch、RCU-style 方案
- **进度保证** — lock-free vs wait-free 的精确声明
- **CAS 循环审查** — weak/strong、success/failure order、retry 行为

## 适用场景

- 实现 lock-free queue、stack、counter
- 审查现有无锁代码的正确性
- 需要证明内存序的正确性
- 设计内存回收方案
- 分析 ABA 暴露

## 不适用

- 仅因 mutex 出现在 profiler 中就切换到无锁（先用 `cpp-concurrency-performance` 诊断）
- 没有明确的 lock-free 需求时

## 调用方式

告诉 agent：

> 用 cpp-lock-free 审查这个 MPSC 队列的内存序和回收策略

或

> 用 cpp-lock-free 帮我设计一个 lock-free stack，要求 wait-free pop
