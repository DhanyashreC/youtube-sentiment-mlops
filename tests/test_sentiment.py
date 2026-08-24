from src.sentiment_analysis import get_sentiment


def test_positive_sentiment():
    assert get_sentiment("I love this song") == "Positive"


def test_negative_sentiment():
    assert get_sentiment("I hate this song") == "Negative"


def test_neutral_sentiment():
    assert get_sentiment("This is a song") == "Neutral"