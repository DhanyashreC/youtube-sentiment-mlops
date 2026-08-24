import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
import pandas as pd

# Load API key from .env file
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

# Connect to YouTube API
youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)


def get_comments(video_id, max_results=100):
    comments = []

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_results,
        textFormat="plainText"
    )

    response = request.execute()

    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)

    return comments


# Test with a YouTube video ID
video_id = "BciiXULbAuo"

comments = get_comments(video_id)

# Convert comments to a DataFrame
df = pd.DataFrame(comments, columns=["comment"])

# Save comments
df.to_csv("data/youtube_comments.csv", index=False)

print(f"Successfully fetched {len(comments)} comments!")
print(df.head())