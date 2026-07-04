# C++ Concurrency Performance

基于证据的多线程 C++ 性能优化。

## 用途

诊断和优化已测量的并发性能问题。前提是并发正确性已建立。

## 核心关注

证据驱动，不靠直觉。

- **scaling curve** — T=1 到多线程的性能曲线
- **瓶颈分类** — contention、scheduling、granularity、imbalance、queueing、locality、false sharing、memory bandwidth、NUMA、oversubscription
- **假设-实验-重测** — 每次只改一个变量
- **benchmark 方法** — 环境记录、重复、raw data 持久化

## 适用场景

- 吞吐量不随线程数增长
- tail latency 爆炸
- CPU 高但吞吐量平
- 性能随线程数增加反而退化
- 需要决定是否值得做无锁优化

## 不适用

- 正确性尚未建立时（先用 `cpp-concurrency-guidelines`）
- 没有测量数据的优化（先建 benchmark）

## 调用方式

告诉 agent：

> 用 cpp-concurrency-performance 诊断这个线程池在 T=8 时的 scaling 退化

或

> 用 cpp-concurrency-performance 帮我建立这个 task system 的 scaling matrix
