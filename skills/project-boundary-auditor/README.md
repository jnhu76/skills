# Project Boundary Auditor

## 这个 skill 是干什么的？

用于分析一个软件项目的真实边界。

它不是总结 README，而是判断：

- 哪些是 bug；
- 哪些是设计边界；
- 哪些是功能缺口；
- 哪些是文档缺失；
- 哪些是环境问题；
- 哪些是用户误用；
- 哪些是技术债；
- 哪些适合 patch；
- 哪些需要 wrap；
- 哪些需要 fork 或 redesign。

## 什么时候用？

适合这些问题：

```text
这个项目到底能不能用？
这是 bug 还是项目边界？
这个项目能不能作为我项目的基础？
这个项目适合 fork 吗？
这个工具只是 sync tool，还是能发展成本地分发中心？
```

## 通用调用 Prompt

你可以把下面这段直接丢给任意 coding agent：

```markdown
请使用 `project-boundary-auditor` skill 分析这个项目。

我的目标不是总结 README，而是判断它的真实边界：

- 哪些是 bug；
- 哪些是设计边界；
- 哪些是功能缺口；
- 哪些是文档缺失；
- 哪些是环境问题；
- 哪些是我的误用；
- 哪些是技术债；
- 哪些适合 patch；
- 哪些需要 wrap；
- 哪些需要 fork 或 redesign。

请严格区分：

```text
文档声称
配置/schema 暗示
代码实际支持
测试覆盖
运行时验证
维护者意图
```

不要把 README 当成事实。
不要把我的需求自动当成项目承诺。
不要泛泛夸奖。
每个判断都要给证据等级和置信度。

我的目标需求是：

```text
<在这里写你的目标>
```

我观察到的问题是：

```text
<在这里写具体问题>
```

我提供的材料包括：

```text
<README / docs / 目录结构 / 配置 / 源码片段 / 测试结果 / issue 链接>
```
```

## 分析 skillshare / SkillDist 的专用调用 Prompt

```markdown
请使用 `project-boundary-auditor` skill 分析 skillshare。

我的目标不是简单同步 skill，而是判断它能不能作为“本地 agent capability 分发中心”的基础。

请重点判断：

1. 它的核心抽象是 sync tool、package manager，还是 control plane？
2. 它的 source / target / mode / extras / audit 是否足够承载 SkillDist？
3. 哪些能力是已有边界内可以 patch 的？
4. 哪些能力需要 wrap？
5. 哪些能力如果要做就必须 fork 或重新设计？
6. 请把问题分类为 bug / design boundary / feature gap / documentation gap / architecture debt。
7. 最后给出 use as-is / configure / patch / wrap / fork / redesign 的建议。
```

## 最小输入材料

最好提供：

```text
README
docs
配置示例
目录结构
关键源码
测试结果
复现步骤
issue / PR 链接
你的目标需求
你观察到的问题
```

## 输出应该包括

```text
一句话定位
核心抽象
契约地图
能力地图
主流程 trace
问题分类
边界测试计划
适配度判断
最终路线：use / configure / patch / wrap / fork / redesign
```
