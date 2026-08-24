import pandas as pd
import matplotlib.pyplot as plt

# Load sentiment data
df = pd.read_csv("data/cleaned_sentiment_results.csv")

# Count sentiments
sentiment_counts = df["sentiment"].value_counts()

print("Sentiment Summary:")
print(sentiment_counts)

# Create bar chart
sentiment_counts.plot(kind="bar")

plt.title("YouTube Comment Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Number of Comments")

plt.tight_layout()

# Save chart
plt.savefig("data/sentiment_chart.png")

plt.show()