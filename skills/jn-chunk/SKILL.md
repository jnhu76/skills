---
name: jn-chunk
description: Split English transcripts into listening chunks with weak forms, linking, stress, shadowing.
origin: hoooo.org
disable-model-invocation: true
---

# English Listening Chunk Trainer

## Purpose

This skill trains listening through chunks.

The goal is to help the learner understand that natural English is not heard word by word. It is heard as meaning groups with stress, weak forms, linking, reduction, and rhythm.

## When to Use

Use this skill when the user provides:

- a listening transcript;
- a sentence they cannot hear clearly;
- a podcast/news/video line;
- a request about chunking, connected speech, weak forms, shadowing, or dictation.

## Input Contract

Expected input:

```text
Transcript:
<English transcript>

Optional:
I cannot hear:
<specific words/sentences>

Optional:
Accent target:
American / British / neutral

Optional:
Speed:
slow / natural / fast
```

If no accent is specified, use neutral General American explanations by default, while noting that real audio may vary.

## Output Contract

### 1. Meaning Overview

Briefly explain the content in Chinese.

### 2. Chunk Splitting

Split each sentence by real listening rhythm, not only grammar.

Format:

```markdown
Original:

Chunk version:
A / B / C / D

Chinese meaning:

Chunk functions:
- A: background
- B: main idea
- C: detail
- D: result/comment
```

### 3. Listening Difficulty Analysis

For likely hard parts, use this format:

```markdown
Original:

May sound like:

Phenomenon:
- linking / weak form / unreleased stop / elision / assimilation / stress / intonation / rhythm

Why it happens:

How to practice:
```

### 4. Weak Forms Table

Find function words such as:

```text
to, of, and, for, can, have, has, was, were, the, a, an, that, in, at, on, from, as, you, your
```

Use this table:

| Word | Natural weak form | Chunk | Practice note |
|---|---|---|---|

Do not force weak forms if the word is stressed in context.

### 5. Stress and Rhythm

For each sentence:

```markdown
Sentence:

Stressed words:

Light words:

Rhythm note:

Chinese explanation:
```

The learner needs to know:

- content words usually carry meaning;
- function words are often reduced;
- contrastive meaning may change stress;
- final important words often receive strong stress.

### 6. Shadowing Script

Generate 3 versions:

#### A. Slow Chunk Version

Use `/` to separate chunks.

#### B. Natural Speed Version

Mark:

- stressed words with **bold**;
- weak/reduced words with `(weak)` when useful;
- linking with `‿` when useful.

Example:

```text
I want‿to / **talk about** / how **models** / are **changing** software development.
```

#### C. Continuous Shadowing Version

Give the full passage with chunk marks only, suitable for repeated reading.

### 7. Dictation Exercises

Generate 3 levels:

#### Beginner

Blank key words.

#### Intermediate

Blank chunks.

#### Advanced

Give Chinese meaning only. Learner writes the English sentence.

### 8. Retelling Practice

Generate:

- 15-second retelling;
- 30-second retelling;
- 60-second retelling.

Retellings should preserve core chunks and sentence patterns from the original.

### 9. Minimal Listening Review List

End with:

```markdown
## 今日听力最小复习清单

### 5 important chunks

### 5 weak forms / linking points

### 5 stressed words

### 3 retelling patterns

### Tomorrow's re-listening plan
```

## Quality Rules

- Do not use IPA unless the user asks for it.
- Use plain sound explanations that a learner can imitate.
- Do not invent exact audio if there is no audio; say “may sound like”.
- Explain that actual pronunciation varies by speaker and accent.
- Keep chunking practical for listening and shadowing.

## Common Mistakes to Avoid

- Do not split only by punctuation.
- Do not mark every function word as weak if it is emphasized.
- Do not overuse pronunciation notation.
- Do not turn listening training into only translation.
- Do not make shadowing scripts too visually complicated.

## Default Daily Limit

For a long transcript, prioritize:

- 5 to 8 key chunks;
- 5 hard-to-hear points;
- 5 weak forms/linking cases;
- 3 retelling patterns.
