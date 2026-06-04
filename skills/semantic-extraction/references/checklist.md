# Semantic Extraction Checklist

Use this checklist before finalizing an analysis.

## First Principles

- [ ] Did I identify the simple baseline?
- [ ] Did I explain why the mechanism is needed?
- [ ] Did I avoid vague goals like “fast”, “safe”, “robust” without observables?

## Operations

- [ ] Did I list primitive operations?
- [ ] Did I avoid treating marketing features as primitives?
- [ ] Did I split overloaded operations?

## Objects

- [ ] Did I distinguish objects/resources?
- [ ] Did I show how the same operation changes meaning on different objects?
- [ ] Did I identify high-risk objects?

## States / Conditions

- [ ] Did I identify lifecycle states or task stages?
- [ ] Did I explain how behavior changes across states?
- [ ] Did I include failure states?

## Observable Effects

- [ ] Did I define what can be measured or logged?
- [ ] Did I include security effects?
- [ ] Did I include performance effects?
- [ ] Did I include recovery effects?

## Rules / Guarantees

- [ ] Did I write at least one `condition → behavior` rule?
- [ ] Did I distinguish allow, deny, log, rollback, escalate?
- [ ] Did I define violation cases?

## Trade-offs

- [ ] Did I identify at least one real trade-off?
- [ ] Did I distinguish sensitive and non-sensitive variables?
- [ ] Did I avoid “best system” thinking?

## Research Gap

- [ ] Did I identify hidden assumptions?
- [ ] Did I identify unclear semantics?
- [ ] Did I suggest experiments with controlled variables?
- [ ] Did I explain why the gap is not just feature implementation?
