# Contribution Planning

## Security Disclosure Rule

If an issue involves default secrets, encryption keys, auth bypass, token leakage, privilege escalation, sandbox escape, RCE, unsafe deserialization, sensitive data exposure, credential storage weakness, or audit/compliance vulnerabilities — do not recommend a public issue or public PR first. Recommend private security disclosure.

A private security disclosure should include: short vulnerability summary, affected component, impact, minimal reproduction or code evidence, suggested fix direction, whether the reporter is willing to help prepare a patch.

## Patchability Score

| Score | Meaning |
|---|---|
| S | Very small patch, <= 3 files, no behavior change outside scope |
| M | Localized behavior change, needs tests |
| L | Cross-module change, migration or compatibility risk |
| XL | Architecture-level change, not suitable for direct PR |

## Acceptance Likelihood

| Level | Meaning |
|---|---|
| High | Small, well-scoped, tested, aligned with project style |
| Medium | Useful but may require maintainer preference or design discussion |
| Low | Large refactor, unclear value, risky migration, broad behavior change |

Prefer high-acceptance PRs for early contribution.

## Public Contribution Rule

Prefer direct PR only when: not security-sensitive, small scope, clear expected behavior, tests/docs can be added, no migration, no broad refactor, fits existing abstractions.

Use issue/discussion first when: behavior may be intentional, fix changes public behavior, multiple designs possible, touches core abstractions, ambiguous contract, compatibility impact.

## First PR Rule

When recommending a first PR, pick exactly one. The first PR should satisfy: no security-sensitive disclosure, touch <= 3 files, include test or doc update, no broad refactor, no behavior change outside scope, easy to review and revert.

## Contribution Plan Output

```markdown
## Contribution Plan

### Disclosure Classification

| Issue | Public Issue | Direct PR | Private Security Advisory | Reason |
|---|---|---|---|---|
| ... | yes/no | yes/no | yes/no | ... |

### PR Slicing

| PR | Title | Scope | Files | Tests | Risk | Patchability | Acceptance Likelihood |
|---|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | low/medium/high | S/M/L/XL | High/Medium/Low |

### First PR Recommendation

Pick exactly one first PR. Explain why this PR first, why safe to do publicly, why likely accepted, files to touch, tests/docs, what not to include.

### Do Not Do Yet

List valid issues not suitable for immediate contribution. Explain why: security sensitivity, migration risk, architecture scope, review burden, unclear maintainer intent, too many files, high conflict risk, needs design discussion.
```
