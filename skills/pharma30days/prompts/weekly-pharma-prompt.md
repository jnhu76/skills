Use the `pharma30days` skill.

Topic: {company_or_asset_or_target}
Lookback: {days} days
Mode: weekly catalyst report

Requirements:

1. Search recent pharma / biotech news using English official sources first.
2. Use Tencent News / Chinese sources only as discovery and market-sentiment inputs unless they cite official evidence.
3. Dynamically build or update the pipeline registry. Do not rely on a fixed watchlist.
4. Cluster duplicated news by event.
5. Map each event to asset, target, indication, clinical phase, regulatory stage, and catalyst type.
6. Score each cluster using the 0-25 catalyst scorecard.
7. Distinguish:
   - short-term stock sentiment
   - medium-term regulatory / BD catalyst
   - long-term commercial fundamentals
8. Explicitly state what changed and what did not change.
9. Flag promotional or recycled stock-site claims.
10. End with the top 3 watchpoints for the next 4-12 weeks.
