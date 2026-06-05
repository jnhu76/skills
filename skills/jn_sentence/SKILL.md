---
name: jn_sentence
description: Extract reusable sentence patterns from an English article so the learner can use them in writing, picture description, oral retelling, and short essays. Use when the user wants to learn sentence structures rather than only translate a passage. Short key for personal invocation.
---

# English Sentence Pattern Miner

## Purpose

This skill extracts reusable sentence patterns from an English article.

The goal is to move from:

```text
I understand this sentence.
```

to:

```text
I can use this sentence pattern to say something of my own.
```

## When to Use

Use this skill when the user provides an English article and asks for:

- 长难句分析;
- 句型提炼;
- 句型迁移;
- 仿写;
- 看图写话;
- 作文句型;
- 口头复述句型.

## Input Contract

Expected input:

```text
Article:
<English article>

Optional:
Unknown words:
<word list>

Optional output target:
- picture description
- 80-word essay
- oral retelling
- exam writing
- technical writing
```

## Output Contract

### 1. Article Language Overview

Briefly identify:

- topic;
- genre;
- tone;
- why the language is worth learning;
- top 3 sentence-level learning points.

Example tones:

- neutral news;
- satire;
- humorous story;
- technical explanation;
- academic argument;
- persuasive essay;
- propaganda-style parody.

### 2. Key Sentence Analysis

For each selected sentence:

```markdown
## Sentence <n>

Original:

Main structure:

Modifiers:

Grammar point:

Chinese translation:

Reusable pattern:

Pattern formula:

When to use it:

3 imitation examples:

1 Chinese-to-English practice:
```

### 3. Pattern Formula Rules

Convert original sentences into reusable formulas.

Examples:

```text
A had improved tremendously, but B remained high.
```

```text
If only A could be a little more/less B.
```

```text
He carried neither A nor B — only C and D.
```

```text
With a/an <sound/event>, A plummeted from B to C.
```

```text
From that day on, A no longer dared to do B recklessly.
```

A good formula should be:

- shorter than the original;
- reusable in other topics;
- clear enough for the learner to imitate;
- useful for writing or speaking.

### 4. Pattern Migration Examples

For each formula, give examples in the learner's likely domains:

- study;
- technology;
- work;
- daily life;
- investment or market observation, when appropriate;
- software projects, when appropriate.

Example:

Original pattern:

```text
A had improved tremendously, but B remained high.
```

Migration examples:

```text
My reading had improved tremendously, but my listening remained weak.
```

```text
The software had improved tremendously, but its memory usage remained high.
```

```text
The company had grown tremendously, but its debt remained high.
```

### 5. Output Tasks

End with 3 small output tasks:

#### A. Pattern Imitation

Give 5 Chinese sentences. The learner must translate them using today's patterns.

#### B. Picture Description

Describe a picture in words. Ask the learner to write 80 words using:

- 3 patterns;
- 5 vocabulary items;
- 3 chunks or collocations.

#### C. 30-Second Oral Retelling

Provide a skeleton:

```text
Topic:
Background:
Turning point:
Result:
Comment:
```

Require the learner to use 3 sentence patterns.

## Quality Rules

- Do not over-explain grammar if it does not help output.
- Prefer reusable sentence frames over abstract grammar labels.
- Always include imitation examples.
- Always connect patterns to output tasks.
- Keep patterns at the learner's level: CET-6 to IELTS 6.0 by default.
- If a sentence is beautiful but not reusable, mark it as “style only”.

## Common Mistakes to Avoid

- Do not only translate long sentences.
- Do not extract patterns that are too specific to reuse.
- Do not give overly literary examples unless the original text is literary.
- Do not make all examples about generic students; use concrete scenes.

## Default Daily Limit

- 5 to 8 sentence patterns;
- 3 imitation examples per pattern;
- 5 Chinese-to-English exercises;
- 1 picture description task;
- 1 oral retelling skeleton.
