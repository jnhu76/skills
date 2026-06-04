# Bug or Boundary

## 这个 skill 是干什么的？

这是 `project-boundary-auditor` 的轻量版。

用于快速判断一个具体现象是：

- bug
- 设计边界
- 功能缺口
- 文档缺失
- 环境问题
- 用户误用
- 技术债

## 什么时候用？

适合快速判断：

```text
这是 bug 吗？
这是项目边界吗？
是不是我用错了？
这个能不能提 issue？
这个需要 patch 还是 wrap？
```

## 调用 Prompt

```markdown
请使用 `bug-or-boundary` skill 判断下面这个现象。

请不要直接把它定性为 bug。
请先检查它是否违反了项目已有契约。

分类只能从下面选择：

- bug
- design boundary
- feature gap
- documentation gap
- environment issue
- misuse
- technical debt
- hypothesis only

请严格区分：

```text
文档声称
配置/schema 暗示
代码实际支持
测试覆盖
运行时验证
维护者意图
```

观察到的现象：

```text
<写具体现象>
```

我期望的行为：

```text
<写你以为应该发生什么>
```

我提供的证据：

```text
<README / 配置 / 代码 / 测试 / 日志 / 复现步骤>
```

请输出：

1. Observed
2. Expected
3. Contract evidence
4. Classification
5. Confidence
6. Reasoning
7. Next action: use / configure / file issue / patch / wrap / fork / redesign
```
