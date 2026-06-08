# Workflow: Dynamic Pipeline Registry

A pipeline registry is a temporary research object built during each run. It is not a permanent watchlist and not the source of truth.

## Registry fields

```yaml
company:
  chinese_name:
  english_name:
  tickers: []
assets:
  - asset_id:
    names: []
    target:
    modality:
    indications:
      - indication:
        phase:
        trial_names: []
        trial_ids: []
        endpoints: []
        latest_event:
        next_milestone:
    partners: []
    evidence_sources: []
    confidence: high | medium | low
```

## Update rules

- Add assets discovered from official or reputable sources.
- Keep unknown assets as `candidate_asset` until verified.
- If a stage changes, record the event and source.
- If a claim is rejected, record why.
- Do not silently overwrite old information; show a registry update block.
