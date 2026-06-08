# Example: Hengrui ASCO Follow-up Weekly Run

Input:

```text
pharma30days 恒瑞医药 ASCO 2026 ADC --days=7
```

Expected behavior:

1. Resolve Hengrui / Jiangsu Hengrui / 恒瑞医药 / 600276.
2. Resolve ADC assets discovered from current sources, such as SHR-A1811, SHR-A2009, SHR-A2102.
3. Search ASCO / ASCOPubs / Hengrui English releases / ClinicalTrials.gov / Reuters / Fierce / Tencent News.
4. Cluster stories:
   - HER2 ADC colorectal cancer Phase III data
   - HER3 ADC NSCLC Phase III / CDE registration path
   - Nectin-4 ADC MIBC early pCR data
   - competitor ADC events
5. Score each cluster.
6. Explain whether each cluster is true regulatory catalyst, BD optionality, same-target validation, or hype.

Anti-hype examples:

- “ASCO oral presentation” is not the same as approval.
- “pCR improved” is not the same as OS benefit.
- “potential milestone” is not upfront cash.
- “same target competitor success” may validate biology but also increase competitive pressure.
