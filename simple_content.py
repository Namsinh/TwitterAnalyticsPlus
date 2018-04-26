from google.cloud import language
from collections import defaultdict

import os

print os.environ["PATH"]

# Change this path to your local cred.json location ###
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/benjaminwasserman/Desktop/cpsc353/twitter_final/TwitterAnalyticsPlus/credentials.json"

all_categories = []


def category_split(name):
    return name.split("/")


def append_categories(categories):
    all_categories.extend(categories)


def simple_classify(text, verbose=True):
    """Classify the input text into categories. """

    language_client = language.LanguageServiceClient()

    document = language.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT)
    response = language_client.classify_text(document)
    categories = response.categories

    result = {}

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    if verbose:
        print(text)
        for category in categories:
            # print(u'=' * 20)
            # print(u'{:<16}: {}'.format('category', category.name))
            # print(u'{:<16}: {}'.format('confidence', category.confidence))
            long_category = category.name
            append_categories(category_split(long_category))

    return
# [END def_classify]


def print_categories():
    tally = defaultdict(int)
    for x in all_categories:
        tally[x] += 1
    print (tally.items())
    for k, v in tally:
        if (k != ''):
            # sort according to the values and then print the first few
            while (x < 5):
                # print the five greatest



def classify(text, verbose=True):
    """Classify the input text into categories. """

    language_client = language.LanguageServiceClient()

    document = language.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT)
    response = language_client.classify_text(document)
    categories = response.categories

    result = {}

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    if verbose:
        print(text)
        for category in categories:
            print(u'=' * 20)
            print(u'{:<16}: {}'.format('category', category.name))
            print(u'{:<16}: {}'.format('confidence', category.confidence))

    return result
# [END def_classify]
