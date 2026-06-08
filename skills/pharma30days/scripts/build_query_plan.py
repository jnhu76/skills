#!/usr/bin/env python3
"""Generate pharma30days search-query templates for a company/drug/target topic.

This helper does not call the internet. It prints query strings that an agent can feed
into WebSearch or a Tencent News skill.
"""
from __future__ import annotations

import argparse


def build_queries(topic: str, days: int) -> list[str]:
    base = topic.strip()
    return [
        f'{base} clinical trial results last {days} days',
        f'{base} FDA EMA NMPA CDE approval submission last {days} days',
        f'{base} ASCO ESMO AACR WCLC data {days} days',
        f'{base} investor presentation press release {days} days',
        f'{base} Reuters Fierce Biotech BioPharma Dive Endpoints {days} days',
        f'{base} 创新药 临床 获批 CDE 出海 授权 过去{days}天',
        f'{base} 腾讯新闻 医药 临床 获批 授权 过去{days}天',
        f'{base} 竞品 靶点 ADC 双抗 III期 PFS OS ORR',
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('topic')
    parser.add_argument('--days', type=int, default=30)
    args = parser.parse_args()
    for q in build_queries(args.topic, args.days):
        print(q)


if __name__ == '__main__':
    main()
