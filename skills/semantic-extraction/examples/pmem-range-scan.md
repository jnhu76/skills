# Example: Extracting Semantics from PMem Range Scan

## 1. First-Principles Goal

PMem exists between DRAM and SSD-like storage. It exposes memory-like access while requiring explicit thinking about persistence, ordering, and recovery.

The research issue is not merely:

```text
PMem is faster than SSD.
```

The real issue is:

```text
How do PMem persistence and ordering semantics change data structure design for range scan workloads?
```

## 2. Primitive Operations

| Operation | Meaning |
|---|---|
| load | read from persistent memory |
| store | write to cache line |
| flush | push cache line toward persistence |
| fence | enforce ordering |
| range scan | read a key interval |
| recover | reconstruct state after crash |

## 3. Objects

| Object | Semantic meaning |
|---|---|
| cache line | persistence granularity |
| index node | traversal cost |
| log entry | recovery evidence |
| key range | scan locality |
| pointer-linked layout | cache miss risk |

## 4. States

| State | Semantic change |
|---|---|
| before flush | write may not survive crash |
| after flush + fence | write may be persistent |
| cold cache | scan dominated by load/cache misses |
| warm cache | scan may hide PMem latency |
| after crash | only persisted writes are valid |

## 5. Rules

| Condition | Operation | Expected behavior |
|---|---|---|
| write without flush/fence | crash recovery | value not guaranteed persistent |
| contiguous layout | range scan | high locality |
| pointer-heavy layout | range scan | cache miss sensitive |
| frequent flush | update | stronger persistence but higher cost |

## 6. Research Gap

Official APIs expose persistence primitives, but they do not directly tell programmers how to design range-scan-friendly persistent data structures.

This creates a gap:

```text
API semantics → programming model → benchmark variables
```
