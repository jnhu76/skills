# Skills Index

## Skill List

| Skill | 用途 | 适合场景 |
|---|---|---|
| `bounded-review-context` | 请求代码审查前生成 scoped Review Context Pack | PR/diff 准备进入 code review 前 |
| `construction-kickoff-supervisor` | 实现前把 Job Card 转成 TDD-ready Job Pack | 长计划准备交给 TDD agent 前 |
| `/grill-me` | 路由模糊想法或已有计划到合适的质询流程（来源：[mattpocock/skills - grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md)） | 想法模糊（→ clarifying）或已有具体设计待挑战（→ grilling） |
| `jn-audit` | 分析软件项目真实边界、契约、bug、缺口 | 判断项目能否作为基础、是否适合 patch/wrap/fork |
| `jn-bug` | 快速判断现象是 bug、边界、缺口还是误用 | 判断具体现象是否值得提 issue |
| `jn-company` | 用中国产业代际框架分析公司 | 分析上市公司/非上市公司投资价值 |
| `jn-sandbox` | 从第一性原则审查 sandbox 系统找 R&D 缝隙 | 审查 microVM、Docker、gVisor、Firecracker 等 |
| `jn-semantic` | 从技术系统、论文、API、运行时提取语义 | 分析系统并发现研发缝隙、设计实验 |
| `jn-vocab` | 从英文文章生成可复习词卡和 Anki TSV | 阅读文章后整理生词 |
| `jn-sentence` | 从英文文章提炼可迁移句型 | 作文、看图写话前积累句型 |
| `jn-chunk` | 分析听力稿 chunk、弱读、连读、重音 | 听不清自然语速时 |
| `jn-feedback` | 批改基于生词、词块、句型的英文输出 | 写完作文、看图写话、复述后 |
| `cpp-core-standards` | C++ Core Guidelines 编码标准 | 写、审查、重构 C++ 代码 |
| `cpp-concurrency-guidelines` | 多线程 C++ 正确性指南 | 线程、任务、工作池、同步设计 |
| `cpp-concurrency-performance` | 多线程 C++ 性能优化 | 可扩展性、吞吐量、尾延迟、争用分析 |
| `cpp-lock-free` | 无锁 C++ 与高级原子内存序 | CAS、内存回收、线性化点、弱序推理 |
| `pharma30days` | 近 N 天医药/生物科技新闻研究 | 周报监控创新药公司 |
| `writing-coach` | 有状态的写作教学，用 Markdown 工作区做连续训练 | 需要长期写作训练、作业批改、学习记录 |
| `writing-coach-simple` | 轻量分析型写作诊断和修改 | 只需一次性的草稿诊断和修改 |

## 文件约定

```
<skill-name>/
├── SKILL.md       # agent 执行说明
├── README.md      # 人类导航与调用 prompt
└── reference/     # 参考文件（字典、模板、示例，部分 skill 有）
```

## 命名规则

使用短横线命名。`jn-` 前缀为个人快捷 key。

## 索引策略

skill 少的时候靠这个表格就够了。超过 20 个再考虑 registry.yaml、tags 或分类。
