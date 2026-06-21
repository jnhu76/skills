# Agent Skill Hub

个人 Agent Skill 仓库。

## Skills

| Skill | 用途 |
|---|---|
| `bounded-review-context` | 请求代码审查前生成 scoped Review Context Pack |
| `construction-kickoff-supervisor` | 实现前把 Job Card 转成 TDD-ready Job Pack |
| `jn-audit` | 分析软件项目真实边界：bug、边界、缺口、技术债、贡献策略 |
| `jn-bug` | 快速判断具体现象是 bug、边界、缺口还是误用 |
| `jn-company` | 用中国产业代际框架分析公司，区分真实标的与叙事股 |
| `jn-sandbox` | 从第一性原则审查 AI agent sandbox 系统，找 R&D 缝隙 |
| `jn-semantic` | 从技术系统、论文、API 提取语义模型 |
| `jn-vocab` | 从英文文章生成可复习词卡、搭配、例句和 Anki TSV |
| `jn-sentence` | 从英文文章提炼可迁移句型 |
| `jn-chunk` | 分析听力稿 chunk、弱读、连读、重音和 shadowing |
| `jn-feedback` | 批改基于生词、词块、句型的英文输出 |
| `pharma30days` | 近 N 天医药/生物科技新闻研究 |
| `writing-coach` | 诊断和训练分析型写作：判断、比较、边界、细节 |

## 目录结构

```
skills/<skill-name>/
├── SKILL.md       # agent 执行说明
├── README.md      # 人类导航
└── reference/     # 参考文件（部分 skill 有）
templates/
├── SKILL_TEMPLATE.md
└── SKILL_README_TEMPLATE.md
```
