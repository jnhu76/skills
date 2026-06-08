# Skills Index

这里是所有 skill 的扁平导航。

## Skill List

| Skill | 用途 | 适合场景 |
|---|---|---|
| [`jn_audit`](jn_audit/) | 分析软件项目真实边界、契约、bug、功能缺口、文档缺失和扩展风险 | 判断项目能否作为基础；判断 use / patch / wrap / fork / redesign |
| [`jn_bug`](jn_bug/) | 快速判断一个现象是 bug、设计边界、功能缺口、文档缺失、环境问题、误用还是技术债 | 判断某个具体现象是否值得提 issue 或 patch |
| [`jn_company`](jn_company/) | 通过中国产业代际框架分析公司，判断属于第6/7/8代，区分真实投资标的与叙事股 | 分析上市公司或非上市公司是否具备独立知识产权、全球化扩张、全球资源配置能力 |
| [`jn_sandbox`](jn_sandbox/) | 分析AI agent沙箱系统，从第一性原理发现可信的R&D或研究缝隙 | 审查微VM、Docker、gVisor、bubblewrap、Firecracker等沙箱项目 |
| [`jn_semantic`](jn_semantic/) | 从技术系统、论文、基准测试、API、运行时、数据库、存储系统和agent工作流中提取语义 | 分析系统并发现研究缝隙、设计实验 |
| [`jn_vocab`](jn_vocab/) | 从英文文章和生词列表生成可复习词卡、搭配、例句和 Anki TSV | 阅读文章后整理生词、导入生词本 |
| [`jn_sentence`](jn_sentence/) | 从英文文章提炼可迁移句型 | 作文、看图写话、口头复述前积累句型 |
| [`jn_chunk`](jn_chunk/) | 分析听力稿 chunk、弱读、连读、重音和 shadowing 跟读 | 听不清自然语速、词粘在一起时 |
| [`jn_feedback`](jn_feedback/) | 批改基于今日生词、词块、句型写出的英文输出 | 写完 80 词作文、看图写话、复述稿后 |
| [`pharma30days`](pharma30days/) | 固定医药/生物科技主题的最近 N 天新闻研究：多源检索、去重聚类、药品/靶点/阶段映射、催化评分和股价影响分层 | 周报监控创新药公司；审计单条医药新闻；跟踪 ASCO/ESMO/AACR、CDE/NMPA/FDA、BD 出海、竞品读出等催化 |

## 文件约定

每个 skill 目录包含：

```text
<skill-name>/
├── SKILL.md    # agent 执行说明
└── README.md   # 人类导航与调用 prompt
```

## 命名规则

使用短横线命名：

```text
jn_audit
jn_bug
jn_company
jn_sandbox
jn_semantic
jn_vocab
jn_sentence
jn_chunk
jn_feedback
pharma30days
```

不要使用：

```text
Project Boundary Auditor
bug_or_boundary
bugOrBoundary
my skill
```

## 什么时候需要分类？

skill 少的时候，直接靠这个 README 表格就够了。

等 skill 变多，比如超过 20 个，再考虑增加：

```text
registry.yaml
tags
scripts
```
