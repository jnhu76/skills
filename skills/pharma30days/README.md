# pharma30days

`pharma30days` is a domain-specific recent-news skill for pharmaceutical and biotech innovation-drug monitoring.

It borrows the recent-window, multi-source, cluster-first idea from `last30days`, but fixes the topic to pharma / biotech and replaces social engagement scoring with clinical, regulatory, commercial, and stock-catalyst scoring.

## What it does

Given a company, drug, target, indication, or event, it:

1. searches recent pharma news, default 30 days;
2. uses English official sources and fixed pharma media sources as the evidence backbone;
3. optionally uses Tencent News / Chinese financial media as discovery sources;
4. cleans and clusters duplicated news;
5. maps each cluster to drugs, trials, phases, regulatory milestones, and competitors;
6. scores the catalyst strength;
7. explains likely short-term stock sentiment, medium-term catalyst path, and long-term fundamental impact.

## Example invocations

```text
pharma30days 恒瑞医药 --days=7
pharma30days SHR-A1811 --days=30
pharma30days HER3 ADC 中国创新药 --days=30
pharma30days 百济神州 BTK --days=14
pharma30days ASCO 2026 恒瑞 ADC
```

## Recommended use cases

- weekly innovation-drug stock monitoring
- single news audit
- ASCO / ESMO / AACR follow-up tracking
- CDE / NMPA / FDA regulatory catalyst tracking
- BD / overseas licensing impact analysis
- competitor readout monitoring

## Why it avoids a fixed watchlist

A fixed watchlist becomes stale quickly. This skill treats seed lists as recall helpers only. It dynamically builds or updates a pipeline registry from current official sources during each run.

## Tencent News integration

When a Tencent News skill or appkey-based connector is available, use it for Chinese discovery:

- company Chinese name
- drug code / Chinese name
- target + `ADC` / `双抗` / `临床`
- `CDE` / `获批` / `受理` / `医保` / `授权` / `出海`

Tencent results should not be final evidence unless corroborated by official, conference, regulatory, or reputable media sources.

## Files

```text
skills/pharma30days/
├── SKILL.md
├── README.md
├── source-packs/
├── workflows/
├── templates/
├── schemas/
├── prompts/
├── examples/
└── scripts/
```
