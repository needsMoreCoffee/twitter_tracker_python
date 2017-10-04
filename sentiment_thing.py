# -*- coding: utf-8 -*-

from google.cloud import language
from urllib import quote_plus

# from twitter import Twitter


class Analysis:
    """A helper for analyzing company data in text."""

    def __init__(self):
        self.gcnl_client = language.Client()

    def get_sentiment(self, text):
        """Extracts a sentiment score [-1, 1] from text."""

        if not text:
            print("No sentiment for empty text.")
            return 0

        document = self.gcnl_client.document_from_text(text)
        sentiment_thing = document.analyze_sentiment()

        return sentiment_thing.sentiment.score

    def convertscore(self, score):
        if score < 0:
            print("Text is negative")
        if score == 0:
            print("Text is neutral")
        if score > 0:
           print("Text is positive")
