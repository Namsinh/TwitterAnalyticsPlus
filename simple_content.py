from google.cloud import language
from collections import defaultdict

import os
import sentiment

# Change this path to your local cred.json location ###
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

all_categories = []
categorized_text = {}


def category_split(name):
    return name.split("/")


def append_categories(categories):
    all_categories.extend(categories)


def text_categories(categories_delimit, text):
    categories = []
    categories = categories_delimit.split("/")
    for x in categories:
        if (x in categorized_text):
            if (x != ''):
                old_value = categorized_text[x]
                new_value = old_value + text
                del categorized_text[x]
                categorized_text[x] = new_value
        else:
            if (x != ''):
                categorized_text[x] = text


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
        # print(text)
        for category in categories:
            long_category = category.name
            append_categories(category_split(long_category))
            text_categories(long_category, text)
            # print (category.name)

    return
# [END def_classify]


def sort_key(d):
    for x in d:
        return d[x]


# going to need to use something else here
def print_categories():

    count_dictionary = {}

    for x in all_categories:
        y = x
        count = 0
        for z in all_categories:
            if (z == y):
                count += 1
        count_dictionary[y] = count

    del count_dictionary['']

    list_with_count = [{k: v} for (k, v) in count_dictionary.iteritems()]

    list_with_count = (sorted(list_with_count, key=sort_key, reverse=True))

    i = -1

    print
    print ("See the categories that your users tweet about most often and the sentiment below!")
    print

    while (i < 5):
        i += 1
        if (i == 0):
            high_category1 = str(''.join(list_with_count[i].keys()))
            print ("1st: " + high_category1)
            sentiment.classify_sentiment(categorized_text[high_category1].encode('utf-8'))
            print
        elif (i == 1):
            high_category2 = str(''.join(list_with_count[i].keys()))
            print ("2nd: " + high_category2)
            sentiment.classify_sentiment(categorized_text[high_category2].encode('utf-8'))
            print
        elif (i == 2):
            high_category3 = str(''.join(list_with_count[i].keys()))
            print ("3rd: " + high_category3)
            sentiment.classify_sentiment(categorized_text[high_category3].encode('utf-8'))
            print
        elif (i == 3):
            high_category4 = str(''.join(list_with_count[i].keys()))
            print ("4th: " + high_category4)
            sentiment.classify_sentiment(categorized_text[high_category4].encode('utf-8'))
            print
        elif (i == 4):
            high_category5 = str(''.join(list_with_count[i].keys()))
            print ("5th: " + high_category5)
            sentiment.classify_sentiment(categorized_text[high_category5].encode('utf-8'))
            print
