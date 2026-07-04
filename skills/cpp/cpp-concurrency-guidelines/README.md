# C++ Concurrency Guidelines

多线程 C++ 正确性指南，基于 C++ 内存模型和 Core Guidelines CP 规则。

## 用途

设计、写、审查、重构正确的多线程 C++ 代码。

## 核心关注

正确性 > 性能。本 skill 不是性能调优，也不授权投机性无锁编程。

- **并发设计** — 任务、所有权、生命周期
- **同步** — mutex、condition_variable、atomic 的正确使用
- **发布与观察** — happens-before、synchronizes-with
- **关闭语义** — drain、cancel、cooperative shutdown
- **失败传播** — 异常不能逃逸线程函数

## 适用场景

- 线程池、工作池、executor 设计
- 共享队列、状态机的同步设计
- mutex/condition_variable 审查
- shutdown 竞争分析
- worker 生命周期管理

## 调用方式

告诉 agent：

> 用 cpp-concurrency-guidelines 审查这个线程池的 shutdown 语义

或

> 用 cpp-concurrency-guidelines 帮我设计一个 MPSC 队列
