# Agent Skill Hub

个人 Agent Skill 仓库。

这个仓库用来保存、迭代、管理你自己设计的 `SKILL.md`。

## 目录结构

```text
agent-skill-hub/
├── README.md
├── skills/
│   ├── README.md
│   ├── project-boundary-auditor/
│   │   ├── README.md
│   │   └── SKILL.md
│   └── bug-or-boundary/
│       ├── README.md
│       └── SKILL.md
├── templates/
│   ├── SKILL_TEMPLATE.md
│   └── SKILL_README_TEMPLATE.md
├── CHANGELOG.md
└── .gitignore
```

## 核心原则

### 1. `skills/` 扁平排布

所有 skill 直接放在：

```text
skills/<skill-name>/SKILL.md
```

不要按 `research/`、`coding/`、`writing/` 再嵌套。

原因：

- 很多 agent skill loader 默认扫描 `skills/*/SKILL.md`；
- 扁平结构更容易复制、软链接、同步；
- 分类可以写在 README 里，不需要用目录层级表达。

### 2. 每个 skill 目录放两个文件

```text
skills/<skill-name>/
├── SKILL.md    # 给 agent 看的执行协议
└── README.md   # 给人看的说明、调用方式、示例 prompt
```

简单说：

```text
SKILL.md  = 能力本体
README.md = 使用说明
```

### 3. 先不要自动化

第一版不放：

```text
scripts/
registry.yaml
```

原因：

- 现在 skill 数量少；
- 手动复制/软链接更清楚；
- 自动分发逻辑还没定；
- 过早加机器索引会让仓库看起来复杂。

等以后 skill 多了，再加：

```text
scripts/install-global.sh
registry.yaml
```

## 当前 Skills

| Skill | 用途 |
|---|---|
| [`project-boundary-auditor`](skills/project-boundary-auditor/) | 分析软件项目真实边界，判断 bug / 边界 / 功能缺口 / 技术债 |
| [`bug-or-boundary`](skills/bug-or-boundary/) | 快速判断一个具体现象是 bug、边界、误用、环境问题还是功能缺口 |

## 新增一个 skill

```bash
mkdir -p skills/my-new-skill
cp templates/SKILL_TEMPLATE.md skills/my-new-skill/SKILL.md
cp templates/SKILL_README_TEMPLATE.md skills/my-new-skill/README.md
```

然后更新：

```text
skills/README.md
CHANGELOG.md
```

## 推荐提交方式

```bash
git init
git add .
git commit -m "init personal agent skill hub"
```

以后每次修改一个 skill：

```bash
git add skills/project-boundary-auditor/
git commit -m "refine project boundary auditor skill"
```

## 一句话

```text
先把 skill 当成可维护的知识资产，而不是一堆散落的 prompt。
```
