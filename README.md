# AI-Powered Social Media Engagement Dashboard

A complete, industry-oriented digital marketing analytics project that
collects social media engagement data, applies AI-powered sentiment
analysis and content scoring, and visualizes performance trends to
guide content strategy and brand growth decisions.

---

## Objective

To build a digital marketing dashboard that collects social media
engagement data (likes, shares, comments, reach), uses AI-powered
sentiment analysis to classify audience feedback, and visualizes
engagement trends so marketing teams can optimize content strategy and
campaign performance.

---

## Business Problem

Brands and marketing teams post content across multiple platforms but
often lack a single, structured view of what is actually working. Raw
metrics like impressions or follower counts on their own don't reveal
*why* some content outperforms other content. This project solves
that by consolidating post-level data, calculating standardized
engagement KPIs, classifying audience sentiment with AI/NLP, and
surfacing the platforms, content themes, formats, hashtags, and
posting times that drive the strongest results — turning scattered
analytics into a clear content strategy.

---

## Why Social Media Engagement Analytics Matters

Engagement (likes, comments, shares, saves, clicks) is the clearest
signal of whether content is actually resonating with an audience,
rather than simply being seen. Brands, agencies, and growth teams rely
on this kind of analysis to decide where to invest content effort and
ad spend, which formats to keep producing, and which messaging is
falling flat. AI extends this by reading sentiment in comments and
scoring content quality at a scale no human team could match manually,
turning thousands of data points into a short list of decisions.

**Job roles that use dashboards like this:** Digital Marketing
Analyst, Social Media Analyst, Content Strategist, Brand Manager,
Growth Marketer, Marketing Operations Analyst, and Business
Intelligence Analyst.

---

## Dataset Description

**File:** `dataset/social_media_engagement_data.csv`
**Rows:** 120 posts
**Columns:** 21

| Column | Description |
|---|---|
| Post ID | Unique identifier for each post |
| Platform | Instagram, LinkedIn, Facebook, or Twitter/X |
| Post Date | Date the post was published |
| Post Type | Reel, Image, Carousel, Story, Video, or Text Post |
| Content Theme | Educational, Promotional, Behind the Scenes, UGC, Motivational, Product Showcase, Industry News, Event Highlight |
| Caption | The post's caption text |
| Hashtags Used | Hashtag set applied to the post |
| Impressions | Total times the post was displayed |
| Reach | Total unique accounts that saw the post |
| Likes | Number of likes |
| Comments | Number of comments |
| Shares | Number of shares/reposts |
| Saves | Number of saves/bookmarks |
| Profile Visits | Profile visits attributed to the post |
| Link Clicks | Clicks on any link in the post/bio |
| Engagement Rate % | (Likes+Comments+Shares+Saves) / Reach × 100 |
| Follower Growth | Net new followers attributed to the post |
| Sentiment Score | AI-derived sentiment polarity (0–1 scale) |
| AI Content Score | AI-derived content quality score (0–10 scale) |
| Best Posting Time | Historically best-performing time slot for that post |
| Campaign Name | The marketing campaign the post belongs to |

A companion comments dataset (`dataset/comments.csv` and
`dataset/comments_with_sentiment.csv`) provides 150 sample audience
comments used to demonstrate AI sentiment classification at the
comment level.

---

## AI Analysis Logic

Two AI/NLP-driven layers are used in this project:

1. **Comment Sentiment Classification** — `analysis/sentiment_analysis.py`
   uses TextBlob to score the polarity of each comment and classify it
   as **Positive** (polarity > 0.1), **Negative** (polarity < -0.1), or
   **Neutral** (everything in between).
2. **Post-Level Sentiment & AI Content Score** — every post in the main
   dataset carries a `Sentiment Score` (audience sentiment toward that
   post's content/comments) and an `AI Content Score` (a 0–10 rating of
   hook strength, message clarity, emotional appeal, and relevance),
   which together flag which content is both well-received and well
   constructed.

---

## Engagement KPI Framework

| KPI | Formula |
|---|---|
| Total Engagements | Likes + Comments + Shares + Saves |
| Engagement Rate % | Total Engagements / Reach × 100 |
| Click-Through Rate % | Link Clicks / Reach × 100 |
| Avg Sentiment Score | Average of Sentiment Score across posts |
| Avg AI Content Score | Average of AI Content Score across posts |
| Content Performance Score | Composite of Engagement Rate %, Sentiment Score, and AI Content Score |

---

## Analysis Performed

- Social media KPI analysis (Impressions, Reach, Engagement Rate %, CTR, Follower Growth)
- Platform comparison (Instagram vs LinkedIn vs Facebook vs Twitter/X)
- Content theme performance analysis (which themes drive shares/saves)
- Post type / format performance analysis (Reel vs Image vs Carousel vs Video vs Story vs Text)
- Hashtag performance analysis
- Best posting time analysis (heatmap-style)
- Sentiment analysis and distribution (Positive / Neutral / Negative)
- Top 10 and Bottom 10 performing post identification
- AI-based content effectiveness scoring
- Brand growth and follower growth analysis

---

## Dashboard Features

The `dashboard/AI_Social_Media_Dashboard.xlsx` workbook contains 9
sheets:

1. **Dashboard** — the executive view: KPI cards, platform performance
   bar chart, reach trend line chart, content theme bar chart,
   sentiment pie chart, posting-time heatmap table, top 5 posts table,
   and an AI-generated insights panel.
2. **EngagementData** — the full cleaned dataset as a structured Excel
   Table (`tblEngagement`) with calculated Total Engagements,
   Click-Through Rate %, and Sentiment Category columns, with built-in
   filtering on every column.
3. **KPI_Summary** — all headline KPIs and the sentiment distribution
   table, calculated entirely with live formulas.
4. **Platform_Analysis** — engagement metrics grouped by platform.
5. **ContentTheme_Analysis** — engagement metrics grouped by content theme.
6. **PostType_Analysis** — engagement metrics grouped by post format.
7. **PostingTime_Analysis** — average reach/engagement by posting time, with conditional-formatting heatmap.
8. **Hashtag_Performance** — engagement metrics grouped by hashtag set.
9. **TopPosts_Analysis** — Top 10 and Bottom 10 posts ranked by Engagement Rate %, with full tie-breaking logic.

All KPIs and tables are built with live Excel formulas (SUM, AVERAGE,
AVERAGEIF, COUNTIF, LARGE/SMALL, INDEX/MATCH) referencing the raw data
table — no hardcoded numbers — so the dashboard recalculates
automatically if the underlying data changes.

---

## Key Insights

- Facebook and LinkedIn post the highest average engagement rates among the four tracked platforms.
- Educational and Motivational content themes outperform purely Promotional content on engagement rate.
- Reels and Video formats generate stronger shares and saves than static Images.
- Evening posting windows (5 PM–9 PM) and early morning (8–9 AM) show the strongest average reach.
- Positive sentiment (39% of comments) outweighs Negative sentiment (31%), with the remainder Neutral.
- The single highest-performing post combines Video format with an Event Highlight theme on Facebook.
- High impressions do not guarantee high engagement — several high-reach posts rank in the bottom 10 by Engagement Rate %, reinforcing that reach and resonance are different metrics.

---

## Recommendations

1. Shift content mix toward Educational and Motivational themes, which consistently outperform Promotional posts.
2. Prioritize Reels and Video for campaigns where shares and saves (top-of-funnel growth) matter most.
3. Schedule key posts in the 5 PM–9 PM window to maximize reach.
4. Reallocate a larger share of content effort and ad budget toward Facebook and LinkedIn given their stronger average engagement rates.
5. Use AI Content Score and Sentiment Score together during content planning — high AI Content Score with low Sentiment Score signals well-produced content that is still missing the audience's interest.
6. Build a recurring content calendar around the structured hashtag sets and themes shown in the Top 10 performing posts.

---

## Conclusion

This project demonstrates an end-to-end, AI-assisted social media
analytics workflow: from structured data collection and cleaning,
through AI-powered sentiment classification, to a fully formula-driven
Excel dashboard that surfaces actionable content strategy decisions.
It mirrors how a digital marketing agency, in-house brand team, or
growth marketer would monitor and optimize multi-platform content
performance in a real working environment.

---

## Repository Structure

```
AI-Powered-Social-Media-Engagement-Dashboard/
│
├── dataset/
│   ├── social_media_engagement_data.csv
│   ├── comments.csv
│   └── comments_with_sentiment.csv
│
├── analysis/
│   └── sentiment_analysis.py
│
├── dashboard/
│   └── AI_Social_Media_Dashboard.xlsx
│
├── screenshots/
│   └── dashboard_overview.png
│
├── reports/
│   ├── Social_Media_Insights_Report.md
│   └── Strategic_Recommendations_Report.docx
│
├── ai_prompts/
│   ├── AI_Prompts_Used.md
│   └── RefreshDashboard.bas
│
├── README.md
└── Project_Guide_GitHub_LinkedIn.md
```

---

## Tools & Technologies

Excel (formulas, PivotTables, conditional formatting, charts), Python
(pandas, TextBlob for NLP sentiment classification), VBA (automation
macro for dashboard refresh).

---

## Author

Built as a portfolio project demonstrating digital marketing
analytics, AI-powered content analysis, and dashboard design skills
for roles such as Digital Marketing Analyst, Social Media Analyst, and
Business Intelligence Analyst.
