import os
import time
import pandas as pd

from dotenv import load_dotenv
from googleapiclient.discovery import build


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

    # Create YouTube API request
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_results,
        textFormat="plainText"
    )

    # Retry settings
    max_retries = 3
    response = None

    # Try fetching comments
    for attempt in range(max_retries):

        try:
            print(f"Fetching comments... Attempt {attempt + 1}/{max_retries}")

            response = request.execute()

            # If successful, exit retry loop
            break

        except TimeoutError:

            print(f"Request timed out. Attempt {attempt + 1}/{max_retries}")

            if attempt < max_retries - 1:
                print("Retrying in 5 seconds...")
                time.sleep(5)

            else:
                print("Failed to fetch comments after multiple attempts.")
                return []

    # Extract comments
    for item in response.get("items", []):

        comment = (
            item["snippet"]
            ["topLevelComment"]
            ["snippet"]
            ["textDisplay"]
        )

        comments.append(comment)

    return comments


# -------------------------------
# Test with a YouTube video ID
# -------------------------------

video_id = "BciiXULbAuo"

comments = get_comments(video_id)


# Convert comments to DataFrame
df = pd.DataFrame(
    comments,
    columns=["comment"]
)


# Save comments
df.to_csv(
    "data/youtube_comments.csv",
    index=False
)


print(f"\nSuccessfully fetched {len(comments)} comments!")
print(df.head())