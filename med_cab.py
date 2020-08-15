from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


raw_score = SentimentIntensityAnalyzer()


def sentiment_score(sentence: str) -> int:
    sentiment_dict = raw_score.polarity_scores(sentence)
    return (100 + sentiment_dict['compound'] * 101) // 2
