import os
import sys
import time
import pandas as pd

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Fix Unicode/emoji printing on Windows
sys.stdout.reconfigure(encoding="utf-8")


# Load API key from .env file
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")


# Check API key
if not API_KEY:
    print("Error: YOUTUBE_API_KEY is not set.")
    sys.exit(1)


# Connect to YouTube API
youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)


def get_comments(video_id, max_results=100):

    comments = []

    try:
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
                print(
                    f"Fetching comments... "
                    f"Attempt {attempt + 1}/{max_retries}"
                )

                response = request.execute()
                break

            except TimeoutError:

                print(
                    f"Request timed out. "
                    f"Attempt {attempt + 1}/{max_retries}"
                )

                if attempt < max_retries - 1:
                    print("Retrying in 5 seconds...")
                    time.sleep(5)

                else:
                    print("Failed to fetch comments after multiple attempts.")
                    return []

        # If no response was received
        if response is None:
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

    except HttpError as error:

        print("\nYouTube API Error!")

        if error.resp.status == 404:
            print("Video not found or comments are disabled.")

        elif error.resp.status == 403:
            print("Access denied. Check your API key or API quota.")

        elif error.resp.status == 400:
            print("Invalid YouTube Video ID.")

        else:
            print(f"API Error: {error}")

        return []

    except Exception as error:

        print(f"\nUnexpected error: {error}")

        return []


# --------------------------------
# Get Video ID from command line
# --------------------------------

if len(sys.argv) < 2:

    print("Error: Please provide a YouTube Video ID.")
    print("Example:")
    print("python src/get_comments.py 2La6Bk4J2js")

    sys.exit(1)


video_id = sys.argv[1].strip()


if not video_id:

    print("Error: Video ID cannot be empty.")

    sys.exit(1)


# Fetch comments
comments = get_comments(video_id)


# If comments could not be fetched
if not comments:

    print("No comments were fetched.")

    sys.exit(1)


# Convert comments to DataFrame
df = pd.DataFrame(
    comments,
    columns=["comment"]
)


# Create data folder if needed
os.makedirs("data", exist_ok=True)


# Save comments
df.to_csv(
    "data/youtube_comments.csv",
    index=False
)


print(f"\nSuccessfully fetched {len(comments)} comments!")
print(df.head())