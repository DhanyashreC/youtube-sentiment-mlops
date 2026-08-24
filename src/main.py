import subprocess
import sys
from urllib.parse import urlparse, parse_qs


# Fix Unicode/emoji printing on Windows
sys.stdout.reconfigure(encoding="utf-8")


def extract_video_id(user_input):

    user_input = user_input.strip()

    # Direct YouTube Video ID
    if len(user_input) == 11 and "/" not in user_input:
        return user_input

    try:
        parsed_url = urlparse(user_input)

        # Normal YouTube URL
        # https://www.youtube.com/watch?v=VIDEO_ID
        if "youtube.com" in parsed_url.netloc:

            query = parse_qs(parsed_url.query)

            if "v" in query:
                return query["v"][0]

        # Short YouTube URL
        # https://youtu.be/VIDEO_ID
        if "youtu.be" in parsed_url.netloc:

            video_id = parsed_url.path.strip("/").split("/")[0]

            if video_id:
                return video_id

    except Exception:
        return None

    return None


# --------------------------------
# Start Pipeline
# --------------------------------

print("Starting YouTube Sentiment Analysis Pipeline...\n")


# Get user input
user_input = input(
    "Enter YouTube Video URL or Video ID: "
).strip()


# Extract Video ID
video_id = extract_video_id(user_input)


# Validate Video ID
if not video_id:

    print("\nError: Invalid YouTube URL or Video ID.")

    sys.exit(1)


print(f"\nVideo ID detected: {video_id}")


# --------------------------------
# Run get_comments.py
# --------------------------------

print("\nRunning src/get_comments.py...")

result = subprocess.run(
    [
        sys.executable,
        "src/get_comments.py",
        video_id
    ]
)


if result.returncode != 0:

    print(
        "\nPipeline stopped because comments could not be fetched."
    )

    sys.exit(1)


# --------------------------------
# Run remaining pipeline scripts
# --------------------------------

scripts = [
    "src/data_cleaning.py",
    "src/sentiment_analysis.py",
    "src/visualization.py"
]


for script in scripts:

    print(f"\nRunning {script}...")

    result = subprocess.run(
        [
            sys.executable,
            script
        ]
    )

    if result.returncode != 0:

        print(
            f"\nPipeline stopped because of an error in {script}"
        )

        sys.exit(1)


print("\nPipeline completed successfully!")