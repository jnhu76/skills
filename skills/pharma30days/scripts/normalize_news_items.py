#!/usr/bin/env python3
"""Normalize pasted pharma news JSONL items and deduplicate by title/entity/event.

Input JSONL fields are flexible. Output is JSONL with normalized title/source/date.
This is an offline helper for agents that save search results before synthesis.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


def slug_text(s: str) -> str:
    s = re.sub(r'https?://\S+', '', s or '')
    s = re.sub(r'\s+', ' ', s).strip().lower()
    s = re.sub(r'[\W_]+', ' ', s)
    return s.strip()


def stable_id(item: dict[str, Any]) -> str:
    key = '|'.join([
        slug_text(str(item.get('title', ''))),
        slug_text(str(item.get('source', ''))),
        str(item.get('published_at', ''))[:10],
    ])
    return hashlib.sha1(key.encode('utf-8')).hexdigest()[:12]


def normalize(item: dict[str, Any]) -> dict[str, Any]:
    out = dict(item)
    out['title'] = re.sub(r'\s+', ' ', str(out.get('title', '')).strip())
    out['source'] = str(out.get('source', '')).strip()
    out['published_at'] = str(out.get('published_at', '')).strip()
    out['id'] = out.get('id') or stable_id(out)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('input_jsonl')
    parser.add_argument('-o', '--output-jsonl')
    args = parser.parse_args()

    seen = set()
    outputs = []
    for line in Path(args.input_jsonl).read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        item = normalize(json.loads(line))
        key = (slug_text(item.get('title', '')), item.get('source', ''), item.get('published_at', '')[:10])
        if key in seen:
            continue
        seen.add(key)
        outputs.append(item)

    text = '\n'.join(json.dumps(x, ensure_ascii=False, sort_keys=True) for x in outputs) + ('\n' if outputs else '')
    if args.output_jsonl:
        Path(args.output_jsonl).write_text(text, encoding='utf-8')
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
