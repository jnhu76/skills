# Grilling split v1

This package splits the old `grilling` loop into a user-invoked router and two model-invoked sub-skills.

```text
grill-me (user-invoked router)
    |
    +-- intent or observable behavior is not determined --> clarifying (model-invoked)
    |
    +-- a concrete plan/design exists and can be falsified -> grilling (model-invoked)
    |
    +-- task is already determined and there is no material
        plan to challenge -------------------------------> neither
```

The important routing rule is not task size or technical complexity.

Ask:

> Can the intended outcome and externally observable behavior already be determined from the available evidence?

If no, clarify.

If yes, ask whether a concrete proposal exists with premises, boundaries, or trade-offs that can be challenged. If yes, grill it.

If neither condition applies, do not invent a clarification or review session.

## Layout

- `skills/grill-me/SKILL.md` — user-invoked router
- `skills/grill-me/clarifying/SKILL.md` — model-invoked intent clarification sub-skill
- `skills/grill-me/grilling/SKILL.md` — model-invoked plan falsification sub-skill
- `skills/grill-me/router-cases.md` — routing examples for manual/adversarial testing

The two sub-skills are nested under the router. Each has its own `name` and `description` for model invocation. A user-invoked skill can route to model-invoked skills; keeping the two disciplines separate also gives each one its own description and trigger boundary.
