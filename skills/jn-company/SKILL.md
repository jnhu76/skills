---
name: jn-company
description: Analyze a company through the Chinese industrial generation framework, identify whether it belongs to generation 6, 7, or 8, and judge whether it is a real investable candidate or just a narrative stock. Short key for personal invocation.
---

# Company Generation Screener

## Purpose

This skill helps analyze a listed or private company through a Chinese industrial development framework.

The goal is not to decide whether to buy or sell immediately. The goal is to determine:

- which industrial generation the company belongs to;
- whether it has real generation 6 / 7 / 8 characteristics;
- whether it is a true technology / globalization / resource-control company;
- whether it is just using AI, self-reliance, globalization, or new-quality-productivity narratives;
- whether it deserves further investment research.

Core principle:

> A company is not judged by what story it tells, but by whether its capability has turned into revenue, margin, cash flow, pricing power, supply-chain control, or geopolitical resilience.

---

## Industrial Generation Framework

Use the generation model as an analytical lens. For Generations 1-5 background, see `reference/GENERATIONS-1-5.md`.

Focus analysis on Generations 6, 7, and 8.

### Generation 6: Independent Intellectual Property

Core capability: original technology, key patents, core components, self-controlled supply chain, domestic substitution, resistance to sanctions.

Main test: If foreign supply/license/equipment access is restricted, can the company still produce, iterate, and compete?

Main risk: fake self-reliance narrative, patents without product power, R&D without commercial conversion.

### Generation 7: Global Expansion

Core capability: overseas revenue, channels, brands, compliance, manufacturing, global supply-chain management.

Main test: Can the company earn sustainable overseas profit, not just export volume?

Main risk: export without localization, overseas revenue without margin, geopolitical pressure, brand weakness.

### Generation 8: Chinese International Capital / Global Resource Allocation

Core capability: global capital deployment, resource control (mines, energy, ports, logistics), overseas production networks, global standards, long-term contracts.

Main test: Does the company control scarce global resources, channels, production capacity, standards, or strategic infrastructure?

Main risk: political risk, expropriation, sanctions, overseas asset impairment.

---

## Core Task

Classify the company into one or more generations. Most real companies are hybrids.

```text
Primary Generation:
Secondary Generation:
Candidate Future Generation:
Not Yet Proven:
```

---

## Required Input

The user may provide: company name, ticker, industry, products, revenue/profit structure, financial report, investor presentation, news, hypothesis, main concern.

If only a company name is given, analyze cautiously and clearly state what information is missing. Do not invent data.

---

## Analysis Procedure

### Step 1: Business Reality Check

Answer: What does this company actually sell? Who pays? Why do customers buy? What part of the value chain does it control?

Do not start from slogans. Start from business reality.

### Step 2: Generation Classification

Classify using the generation framework. For each relevant generation:

```text
Generation:
Evidence:
Counter-evidence:
Confidence: High / Medium / Low / Not enough evidence
```

### Step 3: Gen 6 / 7 / 8 Capability Test

**Gen 6 Test**: Does the company have core technology that enters the main product, reduces cost, improves margin, or creates customer dependence? Can it survive foreign restriction?

Classification: True Gen 6 / Partial Gen 6 / Narrative Gen 6 / Not Gen 6

**Gen 7 Test**: Does the company have overseas revenue that is growing, with healthy margin, channels, localization, and pricing power?

Classification: True Gen 7 / Partial Gen 7 / Export-only Gen 7 / Narrative Gen 7 / Not Gen 7

**Gen 8 Test**: Does the company control overseas resources, mines, energy, ports, logistics, strategic infrastructure? Can it allocate capital globally?

Classification: True Gen 8 / Partial Gen 8 / Early Candidate / Narrative Gen 8 / Not Gen 8

---

### Step 4: Investable Category Test

**Category A**: Technology that improves cost or margin. Worth studying if technology changes cost structure, yield, margin, customer stickiness, or supply-chain security.

**Category B**: Globalization that improves profit. Worth studying if overseas expansion improves revenue diversity, margin, brand premium, or channel control.

**Category C**: Resource / infrastructure control. Worth studying if it controls energy, minerals, logistics, ports, or strategic infrastructure.

---

### Step 5: Anti-Narrative Filter

For any company using AI, self-reliance, globalization, or policy narratives, apply strict verification. See `reference/ANTI-NARRATIVE.md` for detailed filter questions.

---

### Step 6: Financial Reality Check

Analyze revenue quality, margin quality, cash flow, R&D productivity, overseas quality, and balance-sheet risk. See `reference/ANTI-NARRATIVE.md` for the financial checklist and valuation stress test.

---

### Step 7: Final Classification

Output one of: Ignore / Watchlist / Deep Research / Small Position Candidate / Core Candidate / Too Expensive But Good / Narrative Trap

---

## Judgment Rules

1. **Do not reward slogans.** If a company says it has AI/self-developed/globalization, ask where it appears in financial results.
2. **Do not confuse revenue with power.** Revenue growth is not enough. Look for margin, cash flow, customer dependence, pricing power.
3. **Do not confuse export with globalization.** Export is selling abroad. Globalization is operating abroad.
4. **Do not confuse patents with technology.** A patent matters only if it protects a product, process, cost advantage, or customer lock-in.
5. **Do not confuse good company with good investment.** A company may be excellent but too expensive.
6. **Always identify the failure condition.** Every bullish thesis must include what would prove it wrong.
7. **Separate fact, inference, and speculation.** Use labels: Fact / Inference / Speculation / Unknown.
8. **Prefer hard evidence over narrative.** Audited financials > segment revenue > contracts > verified shipments > management guidance > media > investor presentation > slogan.

---

## Output Format

Use the full report template. See `reference/EXAMPLES.md` for example classifications.

The report should include: one-sentence verdict, business reality, generation classification with evidence, Gen 6/7/8 capability test, investable category test, anti-narrative check, financial reality check, valuation stress test, final classification, next data needed.

---

## Final Reminder

The purpose of this skill is not to predict stock prices. The purpose is to prevent mistaking:

```text
story for capability,
capability for profit,
profit for cash flow,
good company for good investment,
and national narrative for shareholder return.
```
