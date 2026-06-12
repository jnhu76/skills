# jn-sandbox

## 这个 skill 是干什么的？

从第一性原则审查 AI agent sandbox 系统、仓库、论文或设计文档，找出可信的工程缝隙、研究缝隙和实验方向。

它不是列功能清单，也不是默认认为隔离越强越好，而是围绕：

```text
minimum necessary privilege + maximum task capability + bounded execution effects + acceptable latency and overhead
```

判断 sandbox 是否真的提高安全性、可控性和可追踪性。

## 什么时候用？

适合这些场景：

```text
审查一个 sandbox 仓库或论文。
比较 Docker、gVisor、bubblewrap、Firecracker、microVM、rootless container。
为 CapGuard 或 agent sandbox 研究找 R&D gap。
把 README claim 转成 evidence table 或 benchmark plan。
```

## 调用 Prompt

```markdown
请使用 `jn-sandbox` skill 审查下面这个 sandbox 系统。

对象：

<仓库 / 论文 / README / 架构说明>

我的目标：

<例如：找研究缝隙、判断能否用于 agent 执行隔离、设计实验>

请重点回答：

1. 为什么需要 sandbox，它减少了哪些 OS-visible effects；
2. 它保留了哪些 agent 必需能力，牺牲了哪些能力；
3. 它实际提供的是哪种隔离边界；
4. 它依赖哪些 host assumptions；
5. 它的安全性、可用性、性能和部署性 trade-off；
6. 哪些 README claim 需要证据；
7. 能形成哪些可执行实验或研究问题。
```
