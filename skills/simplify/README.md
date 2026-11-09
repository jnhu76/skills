# simplify

面向已能正确工作的代码或 PR 的**证据驱动简化** Skill。降低长期维护成本，优先消除重复实现、推测性防御、无意义抽象和可证实的重复工作；不以代码行数为目标。

## 什么时候用？

- 功能或 Bug 修复完成后，提交 PR 前检查新增的复杂度。
- 审阅 PR，重点寻找重复逻辑、过度设计和没有依据的防御性分支。
- 代码已经正确，但阅读、维护或扩展成本高于必要水平。

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

## 工作方式

1. 阅读仓库的 `AGENTS.md`、相关契约和当前 diff，确定范围。
2. 以 **Reuse / Clarity / Redundant Defenses / Efficiency** 四个维度找候选。
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
