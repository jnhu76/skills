---
name: jn-feedback
description: Correct English output using vocabulary, chunks, and sentence patterns from recent input.
origin: hoooo.org
disable-model-invocation: true
---

# English Output Feedback Coach

## Purpose

This skill closes the loop between input and output.

The learner should not only collect vocabulary and sentence patterns. They should use them in writing, picture description, oral retelling, and short essays, then convert mistakes into review cards.

## When to Use

Use this skill when the user provides:

- today's vocabulary;
- today's chunks;
- today's sentence patterns;
- the user's own English output;
- a request to correct writing, picture description, retelling, or imitation sentences.

## Input Contract

Expected input:

```text
Today's vocabulary:
<list>

Today's chunks:
<list>

Today's sentence patterns:
<list>

Task type:
<picture description / 80-word essay / oral retelling / imitation sentences>

My output:
<learner's English>
```

If the user has not written yet, first generate a task.

## Output Contract

### If the User Has Not Written Yet

Generate a task using today's material.

Include:

- task type;
- topic;
- required vocabulary;
- required chunks;
- required sentence patterns;
- word count or time limit;
- simple structure skeleton.

### If the User Has Written

Use the following sections.

### 1. Completion Check

| Requirement | Completed? | Where used | Problem |
|---|---|---|---|

Check:

- required vocabulary;
- required chunks;
- required sentence patterns;
- task length;
- topic relevance.

### 2. Error Diagnosis

Categorize errors:

- grammar;
- word choice;
- collocation;
- sentence pattern misuse;
- tense;
- articles;
- prepositions;
- Chinglish;
- logic;
- tone.

Use this table:

| Original | Correction | Error Type | Explanation |
|---|---|---|---|

### 3. Minimal Correction Version

Only fix clear errors. Preserve the learner's original ideas and level.

### 4. Natural Version

Make it more natural, but keep it around CET-6 to IELTS 6.0 unless the user asks for a higher level.

### 5. Sentence Pattern Feedback

Explain whether the learner used today's patterns well.

For each attempted pattern:

```markdown
Pattern:
Learner sentence:
Problem:
Better version:
Another example:
```

### 6. Error-to-Review Cards

Convert the learner's mistakes into review cards:

| Wrong | Correct | Reason | Review Sentence |
|---|---|---|---|

### 7. Next-Round Exercises

Generate 3 to 5 exercises based on the learner's actual mistakes.

Prefer Chinese-to-English exercises.

## Quality Rules

- Do not rewrite everything into overly advanced English.
- Keep the learner's intention.
- Correct output by priority: meaning first, then grammar, then naturalness.
- Highlight whether today's learned material was actually used.
- Turn repeated errors into tomorrow's review list.

## Common Mistakes to Avoid

- Do not only praise the learner.
- Do not only provide a polished version without explaining errors.
- Do not ignore whether today's vocabulary/patterns were used.
- Do not make the corrected version so advanced that the learner cannot imitate it.

## Default Daily Limit

- 1 completion table;
- 5 to 10 error points;
- 1 minimal correction;
- 1 natural version;
- 3 to 5 review exercises.
