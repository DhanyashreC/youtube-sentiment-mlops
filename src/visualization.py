import pandas as pd
import matplotlib.pyplot as plt

# Load sentiment results
df = pd.read_csv("data/cleaned_sentiment_results.csv")

# Count sentiments
sentiment_counts = df["sentiment"].value_counts()

print("Sentiment Summary:")
print(sentiment_counts)

# Create chart
plt.figure(figsize=(8, 5))
sentiment_counts.plot(kind="bar")

plt.title("YouTube Comments Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Number of Comments")

# Save chart
plt.savefig("data/sentiment_chart.png")

print("Chart saved successfully as data/sentiment_chart.png")

plt.close()