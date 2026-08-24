import pandas as pd
import re


def clean_comment(comment):
    # Convert to string
    comment = str(comment)

    # Remove extra spaces
    comment = re.sub(r"\s+", " ", comment).strip()

    return comment


def main():
    # Load original comments
    df = pd.read_csv("data/youtube_comments.csv")

    print("Original number of comments:", len(df))

    # Clean comments
    df["clean_comment"] = df["comment"].apply(clean_comment)

    # Remove empty comments
    df = df[df["clean_comment"].str.strip() != ""]

    # Remove duplicate comments
    df = df.drop_duplicates(subset=["clean_comment"])

    print("Comments after cleaning:", len(df))

    # Save cleaned data
    df.to_csv("data/cleaned_comments.csv", index=False)

    print("\nData cleaning completed successfully!")


if __name__ == "__main__":
    main()