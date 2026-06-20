# AI Prompts Used in This Project

This file documents every AI prompt used to build the AI-Powered Social Media
Engagement Dashboard, included for transparency and so the project can be
reproduced or extended.

---

### 1. Dataset Generation
```
Generate a sample dataset for social media engagement with columns
(PostID, Date, Platform, ContentType, Likes, Comments, Shares,
Impressions, PostText) for 50 rows.
```
*(Expanded in this project to 120 rows and 21 columns, including
Engagement Rate %, Sentiment Score, AI Content Score, Best Posting Time,
and Campaign Name, to better reflect a real agency-grade dataset.)*

---

### 2. Engagement Rate Formula
```
Write Excel formulas to calculate Engagement Rate as
(Likes+Comments+Shares)/Impressions for each post.
```

---

### 3. Sentiment Classification (Python / NLP)
```
Generate Python code using TextBlob to classify comments into Positive,
Neutral, or Negative, then export results to a CSV for Excel.
```

---

### 4. KPI Formulas
```
Provide Excel formulas to calculate Total Engagements, Average
Engagement Rate, and % distribution of Positive, Neutral, Negative
comments.
```

---

### 5. Dashboard Layout
```
Suggest a layout for an AI-powered Social Media Dashboard with KPI
cards, engagement trend line chart, sentiment pie chart, and slicers
for platform/content type.
```

---

### 6. Forecasting
```
Write an Excel formula using FORECAST.ETS to predict engagement for
next month based on historical daily engagement data.
```

---

### 7. Automation (VBA)
```
Write a VBA macro to refresh all Power Query connections and
PivotTables in a social media engagement dashboard.
```

---

### 8. AI Image Generator Prompt (for GitHub showcase visual)
```
A modern, professional social media analytics dashboard UI on a dark
navy and teal theme. Top row shows five KPI cards labeled Reach,
Impressions, Engagement Rate, Follower Growth, and AI Content Score.
Middle section shows a bar chart comparing platform performance
(Instagram, LinkedIn, Facebook, Twitter/X), a horizontal bar chart of
content theme performance, and a colorful pie chart for sentiment
distribution (green, yellow, red). Bottom section shows a heatmap-style
table for best posting times and a ranked table of top performing
posts. Clean sans-serif typography, flat design, high contrast,
analytics dashboard aesthetic, 16:9 widescreen, no real brand logos.
```

These prompts can be adapted for ChatGPT, Claude, or any LLM to
regenerate or extend this project with fresh data.
