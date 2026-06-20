"""
AI-Powered Social Media Engagement Dashboard
Step 3: AI-Powered Sentiment Analysis (Comments)

This script uses TextBlob (NLP) to classify social media comments into
Positive, Neutral, or Negative sentiment categories. The output CSV is
designed to be loaded back into Excel and joined against the main
EngagementData table on PostID.

Usage:
    python sentiment_analysis.py
"""

from textblob import TextBlob
import pandas as pd

INPUT_FILE = "comments.csv"
OUTPUT_FILE = "comments_with_sentiment.csv"


def get_sentiment(text):
    """Classify text polarity into Positive / Neutral / Negative."""
    polarity = TextBlob(str(text)).sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"


def get_polarity_score(text):
    """Return the raw polarity score (-1 to 1) for transparency."""
    return round(TextBlob(str(text)).sentiment.polarity, 3)


def main():
    df = pd.read_csv(INPUT_FILE)

    df["PolarityScore"] = df["CommentText"].apply(get_polarity_score)
    df["Sentiment"] = df["CommentText"].apply(get_sentiment)

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Processed {len(df)} comments")
    print(df["Sentiment"].value_counts())
    print(f"\nSaved results to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
