import streamlit as st
import subprocess
import sys
import pandas as pd
from urllib.parse import urlparse, parse_qs


def extract_video_id(user_input):
    user_input = user_input.strip()

    # Direct YouTube Video ID
    if len(user_input) == 11 and "/" not in user_input:
        return user_input

    try:
        parsed_url = urlparse(user_input)

        # Normal YouTube URL
        if "youtube.com" in parsed_url.netloc:
            query = parse_qs(parsed_url.query)

            if "v" in query:
                return query["v"][0]

        # Short YouTube URL
        if "youtu.be" in parsed_url.netloc:
            video_id = parsed_url.path.strip("/").split("/")[0]

            if video_id:
                return video_id

    except Exception:
        return None

    return None


# --------------------------------
# STREAMLIT PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="YouTube Sentiment Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("🎥 YouTube Sentiment Analysis")

st.write(
    "Analyze YouTube comments and discover audience sentiment!"
)


# --------------------------------
# USER INPUT
# --------------------------------

youtube_input = st.text_input(
    "Enter YouTube Video URL or Video ID",
    placeholder="Paste YouTube URL here..."
)


# --------------------------------
# ANALYZE BUTTON
# --------------------------------

if st.button("Analyze Comments"):

    # Check empty input
    if not youtube_input.strip():

        st.warning(
            "Please enter a YouTube Video URL or Video ID."
        )

        st.stop()


    # Extract Video ID
    video_id = extract_video_id(youtube_input)


    # Invalid URL
    if not video_id:

        st.error(
            "Invalid YouTube URL or Video ID. Please try again."
        )

        st.stop()


    # Show detected ID
    st.success(
        f"Video ID detected: {video_id}"
    )


    # --------------------------------
    # RUN PIPELINE
    # --------------------------------

    with st.spinner(
        "Fetching comments and analyzing sentiment..."
    ):

        result = subprocess.run(
            [
                sys.executable,
                "src/main.py"
            ],
            input=video_id + "\n",
            text=True,
            capture_output=True
        )


    # --------------------------------
    # PIPELINE ERROR
    # --------------------------------

    if result.returncode != 0:

        st.error(
            "Unable to analyze this video."
        )

        st.info(
            """
Possible reasons:

• The video does not exist  
• The video is private  
• Comments are disabled  
• The Video ID is invalid  
• YouTube API quota has been exceeded
            """
        )

        # Show technical details only if needed
        with st.expander("Show technical details"):
            if result.stdout:
                st.code(result.stdout)

            if result.stderr:
                st.code(result.stderr)

        st.stop()


    # --------------------------------
    # LOAD RESULTS
    # --------------------------------

    try:

        df = pd.read_csv(
            "data/cleaned_sentiment_results.csv"
        )

    except FileNotFoundError:

        st.error(
            "Analysis results file was not found."
        )

        st.stop()


    # --------------------------------
    # SUCCESS
    # --------------------------------

    st.success(
        "Analysis completed successfully!"
    )


    # --------------------------------
    # SENTIMENT COUNTS
    # --------------------------------

    sentiment_counts = (
        df["sentiment"]
        .value_counts()
    )


    # --------------------------------
    # METRICS
    # --------------------------------

    st.subheader("📈 Sentiment Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "😊 Positive",
        sentiment_counts.get("Positive", 0)
    )

    col2.metric(
        "😐 Neutral",
        sentiment_counts.get("Neutral", 0)
    )

    col3.metric(
        "😞 Negative",
        sentiment_counts.get("Negative", 0)
    )


    # --------------------------------
    # TOTAL COMMENTS
    # --------------------------------

    st.metric(
        "Total Comments Analyzed",
        len(df)
    )


    # --------------------------------
    # CHART
    # --------------------------------

    st.subheader("📊 Sentiment Distribution")

    chart_data = pd.DataFrame(
        {
            "Sentiment": sentiment_counts.index,
            "Comments": sentiment_counts.values
        }
    )

    st.bar_chart(
        chart_data,
        x="Sentiment",
        y="Comments"
    )


    # --------------------------------
    # COMMENTS TABLE
    # --------------------------------

    st.subheader("💬 Analyzed Comments")

    st.dataframe(
        df[
            [
                "clean_comment",
                "sentiment"
            ]
        ],
        use_container_width=True
    )