# This file has two core functions, classify_average and classify_sentiment.
# classify_average categorizes the text passed in and returns a sentiment score
# and a sentiment magnitude. This is used in simple_content.py to determine an
# average sentiment and magnitude for all the people a user follows.
# classify_sentiment works in a similar manner, but merely prints the
# results for the top categories.

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"


def classify_average(text):
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    # print('Text: {}'.format(text))
    return (str(sentiment.score) + "," + str(sentiment.magnitude))


def classify_sentiment(text):
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    # print('Text: {}'.format(text))
    print('Sentiment: score: {}, magnitude: {}'.format(
        sentiment.score, sentiment.magnitude))


# classify_sentiment("I hate this so much!")
