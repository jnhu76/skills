# C++ Skills

C++ 相关 skill 集合，覆盖编码标准、并发正确性、性能优化和无锁编程。

## Skill 依赖关系

```
cpp-core-standards          ← 编码基础，所有 C++ 工作的起点
    │
    ├── cpp-concurrency-guidelines  ← 并发正确性
    │       │
    │       └── cpp-concurrency-performance  ← 性能优化（需要正确性已建立）
    │               │
    │               └── cpp-lock-free  ← 无锁专家领域（需要性能动机）
```

## Skill List

| Skill | 用途 | 适合场景 |
|---|---|---|
| `cpp-core-standards` | C++ Core Guidelines 编码标准 | 写、审查、重构 C++ 代码 |
| `cpp-concurrency-guidelines` | 多线程 C++ 正确性指南 | 线程、任务、工作池、同步设计 |
| `cpp-concurrency-performance` | 多线程 C++ 性能优化 | 可扩展性、吞吐量、尾延迟、争用分析 |
| `cpp-lock-free` | 无锁 C++ 与高级原子内存序 | CAS、内存回收、线性化点、弱序推理 |

## 文件约定

```
cpp/
├── README.md                      # 本文件
├── <skill-name>/
│   ├── SKILL.md                   # agent 执行说明
│   └── README.md                  # 人类导航与调用 prompt
```
