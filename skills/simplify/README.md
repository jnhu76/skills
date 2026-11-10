# simplify

面向已能正确工作的代码或 PR 的**证据驱动简化** Skill。降低长期维护成本，优先消除重复实现、推测性防御、无意义抽象和可证实的重复工作；不以代码行数为目标。

## 什么时候用？

- 功能或 Bug 修复完成后，提交 PR 前检查新增的复杂度。
- 审阅 PR，重点寻找重复逻辑、过度设计和没有依据的防御性分支。
- 代码已经正确，但阅读、维护或扩展成本高于必要水平。
- **既有测试套件清理：**主动比较跨文件、跨层级的用例，删除有证据证明无独立故障检测价值的测试或重复 fixture，而不仅是取消 Coverage 插桩。

不适合用于：尚未理解行为契约的代码、与当前任务无关的全仓重构、以跳过测试或删除必要权限/事务校验换取简洁的场景。

## 使用方法

将 `skills/simplify` 放入 Coding Agent 的 Skill 搜索路径，或将 `SKILL.md` 提供给支持 Skills 的 Agent。根据使用的工具调用：

```text
/simplify
/simplify focus on defensive programming
/simplify focus on PR #929
```

也可明确区分只读评审与授权修改：

```text
使用 simplify 审查当前 PR 的 diff，重点查找重复实现与无依据的 guards。
仅评审，不修改代码。
```

```text
使用 simplify 对当前已通过测试的改动做最小必要重构。
保持合法输入与受支持失败模式的契约行为；保留独立的授权、并发、事务与持久化保护；仅删除已证明不可达的非契约性分支。
仅修改当前任务相关文件，运行受影响的测试，并报告验证结果。
```

## 测试资产精简：两种模式

`focus tests`：**只进行可以证明的无损精简**，检查完整的指定套件而非只看当前 diff，删除重复用例、合并参数/断言/fixture；必须说明保留测试如何检测同一故障。

`focus test-portfolio`：进一步审查“正确且具有独立检测能力的测试，是否值得长期维护”。采用 **KEEP requires justification**，但这是一项风险与成本评审，**不是看到低价值测试就自动删除**。

| 裁决 | 含义 | 默认执行权限 |
|---|---|---|
| `DELETE_REDUNDANT` | 已证明没有独立的必要故障检测能力 | 获授权可修改 |
| `CONSOLIDATE` | 合并测试/fixture，保留必要检测 | 获授权可修改 |
| `DROP_OBSOLETE` | 所保护行为不再属于当前权威契约 | 先核实契约；改变产品行为另需授权 |
| `DROP_LOW_VALUE` | 有独立检测，但风险收益不足以支持长期维护 | **只能提案；必须单独接受丢失的检测能力** |
| `KEEP_CRITICAL` | 独立安全、事务、并发、恢复等重要契约的检测 owner | 保留 |
| `UNPROVEN` | 证据不足、权威不清或缺少风险授权 | 保留 |

重点检查单元测试（非平凡业务性质 vs 实现镜像）、属性测试（真正有价值的不变量 vs 同义例子）、冒烟测试（真实接线 vs 每页重复打开）、API/数据库/浏览器测试（独立信任边界 vs 逐层复制业务规则）。

**不是所有独立测试都必须永久保留，但不能谎称放弃某项检测不会带来损失。** `DROP_LOW_VALUE` 必须记录失去的信号、故障影响、节省的成本、仍然存在的其他信号和需要谁批准。通用的 APPLY 授权不能代替风险接受。已有仓库测试政策、Accepted ADR 优先。

调用示例：

```text
/simplify focus tests in apps/api and apps/web
/simplify focus test-portfolio in apps/api and apps/web
```

停手同样是合理结果：无删除配额，不因测试通过或覆盖率高就自动保留，也不因测试多就强行删。

## 工作方式

1. 阅读仓库的 `AGENTS.md`、相关契约和当前 diff，确定范围。
2. 以 **Reuse / Clarity / Redundant Defenses / Efficiency** 四个维度找候选；测试任务按需运行 `focus tests` 或 `focus test-portfolio`。
3. 特别检查：同一信任区重复校验、必填字段的过度可选链、静默兜底、无价值异常中转。
4. 建立实际调用路径与运行时可信前提；分类为 `PROVEN_REDUNDANT`、`INDEPENDENT_BOUNDARY`、`UNPROVEN`。
5. 获得修改授权后逐项简化并验证；没有合理候选时输出 `NO_CHANGE`。

小改动默认单 Agent；多 Agent、CRAP、重复度工具和 mutation testing 仅在必要时使用，不强制引入额外流程。

## 不可达防御的证明门槛

允许删除针对**已证明不可能触发且非受支持契约**的分支和报错；但 TypeScript 类型声明不等于运行时保证。需要沿调用路径确认真正的解析/验证 owner，并排除来自 JS、反序列化、数据库、类型断言、并发和部分初始化的破坏路径。

**单一语义权威不等于单一执行校验点**：独立认证、授权、状态转换、事务与持久化边界必须保留必要检查。证明不足则输出 `UNPROVEN`，不强行修改。

## 设计参考

- [Claude Code /simplify（社区整理）](https://github.com/noelzappy/claude-code-system-prompts/blob/main/prompts/19_simplify_skill.md)
- [Addy Osmani: code-simplification](https://github.com/addyosmani/agent-skills/blob/main/skills/code-simplification/SKILL.md)
- [avoid-overkill](https://github.com/6Kmfi6HP/avoid-overkill)
- [Uncle Bob: ub-mode](https://github.com/unclebob/ub-mode)

以上仅为设计参考，不是运行时依赖。
