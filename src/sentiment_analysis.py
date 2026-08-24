import sys
sys.stdout.reconfigure(encoding="utf-8")

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the comments
df = pd.read_csv("data/cleaned_comments.csv")

# Create sentiment analyzer
analyzer = SentimentIntensityAnalyzer()


def get_sentiment(comment):
    score = analyzer.polarity_scores(str(comment))

    compound = score["compound"]

    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"


# Apply sentiment analysis to every comment
df["sentiment"] = df["clean_comment"].apply(get_sentiment)

# Save results
df.to_csv("data/cleaned_sentiment_results.csv", index=False)
# Show results
print(df.head(10))

# Show sentiment counts
print("\nSentiment Summary:")
print(df["sentiment"].value_counts())

print("\nAnalysis completed successfully!")