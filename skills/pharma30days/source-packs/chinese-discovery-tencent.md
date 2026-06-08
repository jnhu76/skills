# Chinese Discovery Source Pack: Tencent News and Chinese Pharma / Finance Media

Use Chinese sources mainly for discovery, sentiment, and local market reaction.

## Tencent News

Preferred when a Tencent News skill / connector exists:

- Endpoint / entry: https://news.qq.com/exchange?scene=appkey
- Role: Chinese news discovery, duplicate headline collection, market-language detection
- Do not treat it as primary evidence unless it points to official filings or company announcements.

## Chinese query templates

```text
{公司中文名} 创新药 过去一周
{公司中文名} {药物代码} 临床
{公司中文名} {靶点} ADC
{公司中文名} CDE 受理 获批
{公司中文名} 出海 授权 首付款 里程碑
{公司中文名} ASCO ESMO AACR 数据
{公司中文名} 医保 价格 放量
{药物中文名或代码} III期 PFS OS ORR
```

## Chinese source examples

- 腾讯新闻
- 财联社
- 证券时报
- 中国证券报
- 上海证券报
- 医药魔方
- Insight 数据库新闻
- 药智网
- 36氪
- 界面新闻
- 澎湃新闻

## Red flags in Chinese stock news

Down-rank articles that:

- repeat old conference data as if new;
- emphasize “全球首款 / 全球领先” without regulatory proof;
- confuse pCR with cure rate;
- confuse potential milestones with cash received;
- use “重磅 / 爆发 / 颠覆 / 估值重塑” without primary evidence;
- cite no trial ID, no endpoint, no comparator, no event date.
