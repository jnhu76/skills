# De-abstracting Checklist

## Rule

Every large abstract term must be pushed down one level into concrete actors, actions, objects, or failure modes.

## Common replacements

| Abstract word | Push down into |
|---|---|
| 生态 | 应用、库、驱动、SDK、文档、开发者、客户导入、工具链 |
| 战略窗口 | 原来做不起，现在有机会做；原来没人愿意迁移，现在迁移成本下降 |
| 迁移成本 | 编译错误、依赖缺失、宏不兼容、汇编重写、测试失败、性能回退 |
| 试错成本 | 改一版、跑一遍、失败后看日志、定位、再改、再跑 |
| 平台能力 | 流程、脚本、测试、知识库、模板、工具、自动化检查 |
| 赋能 | 具体是谁能做以前做不了的什么事情 |
| 重塑 | 竞争焦点从什么转向什么 |
| 范式变化 | 原来的流程是什么，新流程是什么，中间成本怎么变 |

## Diagnostic questions

After writing a paragraph, ask:

1. Who is acting?
2. What cost goes down?
3. How exactly does it go down?
4. What feedback loop makes iteration possible?
5. Who enters because of the lower cost?
6. What becomes cheap or commoditized?
7. What remains scarce?

## Bad pattern

> AI 将重塑 RISC-V 生态，打开战略窗口，推动产业范式变化。

Problem: large words, no mechanism.

## Better pattern

> AI Agent 能把跨 ISA 迁移里的编译错误、依赖适配、宏替换和测试失败串成自动循环。这样一来，原来只有少数熟悉工具链的人能做的适配工作，会被更多团队尝试。门槛下降后，基础移植能力会变得不稀缺，竞争会转向性能、可靠性和客户导入。
