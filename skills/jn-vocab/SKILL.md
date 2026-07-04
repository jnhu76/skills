---
name: jn-vocab
description: Build vocabulary cards from English articles — base forms, collocations, Anki export.
origin: hoooo.org
disable-model-invocation: true
---

# English Vocab Card Builder

## Purpose

This skill turns unknown words from an English article into reviewable, usable vocabulary cards.

The goal is not to dump dictionary entries. The goal is to help the learner understand each word in context, know how it changes form, know what it commonly combines with, and reuse it in writing, picture description, retelling, or listening review.

## When to Use

Use this skill when the user provides:

- an English article, paragraph, transcript, or excerpt;
- a list of unknown words;
- a request such as “整理生词”, “还原单词原型”, “做成生词本”, “导入 Anki”, “帮我学这些词”.

## Input Contract

Expected input:

```text
Article:
<English text>

Unknown words:
<word list>

Optional:
- target level: CET-4 / CET-6 / IELTS 6.0 / etc.
- output format: Markdown / TSV / JSON / Anki
- learner's own example sentences
```

If the user gives inflected forms, always restore the base form.

Examples:

- `subsidies` -> `subsidy`
- `postponed` -> `postpone`
- `plummeted` -> `plummet`
- `recklessly` -> `reckless`
- `tremendously` -> `tremendous`

## Output Contract

Always produce these sections unless the user asks for a shorter version.

### 1. Vocabulary Overview Table

Use this table:

| Original | Base Form | POS | Core Meaning | Meaning in Context | Common Collocations |
|---|---|---|---|---|---|

Rules:

- `Original` is the form in the article.
- `Base Form` is the dictionary form.
- `POS` should be practical: n., v., adj., adv., phrase.
- `Meaning in Context` should match the article, not every possible dictionary meaning.
- `Common Collocations` should be usable by the learner.

### 2. Detailed Vocabulary Cards

For each word, output:

```markdown
## <base form>

- Original form:
- Base form:
- Part of speech:
- Core meaning:
- Meaning in this article:
- Word family / inflections:
- Common collocations:
- Usage scene:
- Synonym contrast:
- Original sentence:
- New example:
- Chinese translation:
- Mini practice: translate this sentence into English:
```

### 3. Collocation-Focused Notes

Do not let the learner memorize isolated words only.

For each important word, identify what it usually modifies or combines with:

- verb + noun: `postpone a meeting`, `reduce the price`
- adjective + noun: `massive subsidies`, `intricate details`
- adverb + verb/adjective: `improve tremendously`, `remarkably well`
- noun + preposition: `anxiety about`, `a subsidy for`

### 4. Exportable TSV

Generate a TSV table suitable for Anki or simple vocabulary apps:

```tsv
word	meaning	example	note	tags
```

Rules:

- Use tab characters between fields.
- Keep each card on one line.
- Avoid extra tabs inside fields.
- `word` should be the base form.
- `meaning` should be concise Chinese.
- `example` should be one clear English sentence.
- `note` should include inflections and collocations.
- `tags` should include: `english-vocab`, `article-reading`.

### 5. Minimal Review List

End with:

```markdown
## 今日最小复习清单

### 必背 8 个生词

### 必背 8 个搭配

### 5 个中译英练习
```

## Quality Rules

- Prefer context-specific explanation over dictionary dumping.
- Keep examples close to the learner's likely use cases: study, technology, work, life, markets, projects.
- Explain why a word is used in the article if the tone matters.
- Mark formal / informal / literary / technical usage when relevant.
- If a word is rare or stylistic, say so.
- If a word has a misleading literal meaning, warn the learner.

## Common Mistakes to Avoid

- Do not only translate words into Chinese.
- Do not ignore base forms.
- Do not give examples that are too advanced or unrelated.
- Do not treat all synonyms as interchangeable.
- Do not generate huge word lists if the user only needs a daily review set.

## Default Daily Limit

If there are many words, prioritize:

1. high-frequency words;
2. words central to the article;
3. words useful for output;
4. collocations that can be reused.

Default output size:

- 8 to 12 vocabulary cards;
- 8 collocations;
- 5 translation exercises.
