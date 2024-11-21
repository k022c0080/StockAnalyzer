from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, articles):
        sentiment_scores = [
            self.analyzer.polarity_scores(article['title'] + article['description'])['compound']
            for article in articles if article['title'] and article['description']
        ]
        return np.mean(sentiment_scores) if sentiment_scores else 0
