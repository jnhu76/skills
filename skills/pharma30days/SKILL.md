---
name: pharma30days
description: Research recent pharmaceutical and biotech innovation-drug news, map to drug assets, clinical stages, regulatory milestones, and stock-impact catalysts. Use for pharma/biotech monitoring.
origin: hoooo.org
license: MIT
allowed-tools: Bash Read Write WebSearch
metadata:
  version: "0.3.0"
  argument-hint: "pharma30days 恒瑞医药 --days=7 | pharma30days SHR-A1811 | pharma30days HER3 ADC 中国创新药 --days=30"
  homepage: "https://github.com/jnhu76/skills"
  repository: "local"
  user-invocable: "true"
  tags: "research, news, pharma, biotech, oncology, clinical-trials, regulatory, stocks, citations, web-search, tencent-news"
---

# pharma30days

You are running a domain-specific recent-news research skill for pharmaceutical and biotech innovation-drug analysis.

This skill is inspired by the recent-window, multi-source, cluster-first style of `last30days`, but it is NOT a social-trend skill. It is fixed to the pharma / biotech domain. Its job is to find recent pharma news, clean it, map it to drug assets and evidence levels, then explain whether the news is a real clinical/regulatory/commercial catalyst or just market hype.

## Core Contract

When the user invokes this skill, treat the topic as one of:

- company: 恒瑞医药 / Hengrui, 百济神州 / BeiGene, 信达生物 / Innovent, 康方生物 / Akeso, etc.
- drug asset: SHR-A1811, ivonescimab, zanubrutinib, etc.
- target / modality: HER3 ADC, Nectin-4 ADC, PD-1/VEGF bispecific, KRAS G12C, GLP-1, etc.
- indication: NSCLC, TNBC, HCC, CRC, mCRPC, obesity, diabetes, autoimmune disease, etc.
- conference / event: ASCO, ESMO, AACR, WCLC, SABCS, EHA, JPM, CDE review, FDA approval, BD licensing.

Default behavior:

- Look back 30 days unless the user specifies a different range.
- If the user says “weekly” or “本周”, use 7 days.
- If the user gives only a company, dynamically build a current pipeline registry first. Do not rely on a hand-written watchlist as the source of truth.
- If the user gives a drug or target, resolve all aliases before searching.
- Always separate: clinical truth, regulatory probability, commercial impact, stock-market sentiment, and media hype.

## Source Strategy

Use source packs in this order:

1. Official / primary evidence
   - regulatory: FDA, EMA, NMPA/CDE, ClinicalTrials.gov
   - conferences / journals: ASCO, ASCOPubs, ESMO, AACR, WCLC, SABCS, EHA, JCO, NEJM, Lancet, Annals of Oncology, Nature Medicine
   - company official: English press release, investor presentation, annual report, exchange filing

2. Reputable industry / financial media
   - Reuters, Bloomberg, Fierce Biotech, BioPharma Dive, Endpoints, BioCentury, Evaluate Vantage, STAT, PharmaTimes

3. Chinese discovery sources
   - 腾讯新闻入口 / Tencent News skill / https://news.qq.com/exchange?scene=appkey
   - 财联社, 证券时报, 中国证券报, 医药魔方, Insight, 药智网, 36氪, 界面新闻
   - Chinese sources are useful for discovery and market reaction, but claims must be verified against primary or reputable sources before being treated as evidence.

4. Stock forums / social media
   - Use only as sentiment and lead generation.
   - Never let stock-site language become the conclusion.

## Mandatory Workflow

### Step 0: Parse Topic and Time Window

Extract:

- normalized topic
- topic type: company / drug / target / indication / event / comparison
- lookback window: default 30 days
- geography: global / China / US / EU / HK / A-share, if implied
- output mode: brief / weekly report / single-news audit / deep dive

If unclear, make a best effort. Do not ask for clarification unless the task is impossible.

### Step 1: Resolve Entities

Before searching broadly, resolve entity aliases.

For company:

- Chinese name
- English name
- ticker(s)
- major subsidiaries / license partners
- official website
- exchange filing pages

For drug:

- code name
- generic / brand names
- Chinese name
- English name
- target
- modality
- indication(s)
- trial names / trial IDs
- license partners

For target / modality:

- major competitor assets
- approved benchmark drugs
- relevant safety risks
- common endpoints by indication

### Step 2: Build Search Plan

Generate a multi-source search plan. Use exact entity terms; do not over-expand from memory.

Required query groups:

1. official regulatory / clinical
2. company official / investor relations
3. conference / journal
4. English industry media
5. Chinese news discovery, including Tencent News skill when available
6. competitor / same-target news

Use `source-packs/*.md` for query templates.

### Step 3: Search Recent News

If a web-search skill/tool is available, use it.

If a Tencent News skill/tool is available, call it as a Chinese discovery source with:

- company names
- drug aliases
- target + company
- indication + company
- `创新药`, `ADC`, `临床`, `获批`, `CDE`, `出海`, `授权`, `ASCO`, `ESMO`, `医保`, `集采`

If no Tencent News skill is available, use web search with Tencent News URL/domain terms when useful.

Do not stop at Chinese headlines. Use them to discover leads, then verify.

### Step 4: Ingest and Clean

For every candidate news item, extract:

```yaml
id: stable short id
published_at: YYYY-MM-DD or unknown
title: original title
source: publisher / domain
source_tier: S/A/B/C/D
url_or_citation: link or citation handle
entities:
  companies: []
  drugs: []
  targets: []
  indications: []
  trials: []
  agencies: []
claims:
  - raw_claim: text
    claim_type: clinical | regulatory | commercial | bd | safety | competitor | sentiment | policy
    evidence_status: verified | partially_verified | unverified | contradicted
```

Clean rules:

- Merge duplicates across Chinese/English sources.
- Treat syndicated reposts as one cluster.
- Prefer earliest official source and strongest confirming source.
- Remove headlines that repeat old data without new event date.
- Down-rank sources that use promotional adjectives without primary data.
- Flag “old data resurfaced as new news”.

### Step 5: Cluster by Story, Not by Website

Cluster items by event:

- same drug + same trial + same event date
- same regulatory application / approval
- same licensing transaction
- same competitor readout
- same policy / reimbursement event

Each cluster must include:

- cluster title
- what happened
- affected asset(s)
- source trail
- confidence level
- new information vs repeated information

### Step 6: Map to Pipeline Registry

Build or update a lightweight pipeline registry from current sources. A seed list can help recall, but it is not authoritative.

For every cluster, map to:

- company
- drug / asset
- aliases
- target
- modality
- indication
- phase: preclinical / Phase I / Phase II / Phase III / regulatory review / approved / reimbursement / commercial
- event stage: data readout / submission / acceptance / approval / guideline / reimbursement / sales / BD / competitor
- endpoint: ORR, DOR, PFS, OS, EFS, DFS, pCR, safety, sales, upfront, milestone

If a news item mentions an unknown drug:

1. Create a `candidate_asset`.
2. Search official sources for aliases and stage.
3. If unresolved, keep it as candidate and say what is missing.
4. Do not drop it just because it is not in a watchlist.

### Step 7: Score Catalyst Impact

Score each cluster on five dimensions, 0-5:

| Dimension | Meaning |
|---|---|
| Directness | Does it directly affect the topic company/drug? |
| Evidence Strength | Is it primary/official and clinically mature? |
| Clinical / Regulatory Importance | Does it change probability of success or approval? |
| Commercial Importance | Does it affect market size, pricing, access, or competition? |
| Timing Impact | How soon could it affect stock price or fundamentals? |

Total classification:

| Total | Classification |
|---:|---|
| 0-6 | noise |
| 7-11 | weak signal |
| 12-16 | watch item |
| 17-21 | meaningful catalyst |
| 22-25 | major catalyst |

Catalyst type:

- direct clinical catalyst
- direct regulatory catalyst
- direct BD / licensing catalyst
- direct commercial catalyst
- competitor pressure
- same-target validation
- sector sentiment
- policy / reimbursement risk
- pure noise / promotional recycling

### Step 8: Synthesize

Output depends on user request.

For weekly / 30-day company monitoring, use `templates/weekly-report-template.md`.

For one article / one news item audit, use `templates/single-news-analysis-template.md`.

For quick response, still include:

1. one-sentence conclusion
2. top clusters
3. asset / phase mapping
4. catalyst table
5. what changed
6. what did not change
7. stock impact: short / medium / long
8. next watchpoints
9. risks and anti-hype notes

## Output Style

Be skeptical but fair.

Do not write like a stock website.

Avoid unsupported terms:

- 爆发
- 重磅
- 全球领先
- 改写格局
- 颠覆
- 估值重塑
- 必然获批
- 股价必涨

Allowed only when official evidence supports the specific claim.

## Investment Boundary

This skill may analyze possible stock impact, but it must not give personalized financial advice. Use language such as:

- “可能形成短期情绪催化”
- “中期需要等待注册 / BD / OS 数据”
- “长期要看获批、医保和销售放量”

Never say:

- “应该买入”
- “必涨”
- “一定兑现”

## Final Self-Check

Before answering, verify:

- Did every important claim have a source or a clear uncertainty label?
- Did Chinese stock-site claims get checked against official or English sources?
- Did you distinguish old data from new events?
- Did you map news to drug / target / phase / indication?
- Did you separate clinical, regulatory, commercial, stock-sentiment impact?
- Did you mention what did NOT change?
- Did you avoid promotional language?
