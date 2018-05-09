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
    try:
        response = language_client.classify_text(document)
    except():
        print("Not long enough text to analyze")
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

    return
# [END def_classify]


def sort_key(d):
    for x in d:
        return d[x]


# Going to need to use something else here for the personal tweets - both all_categories and list_with_count are empty in this
def print_categories():

    count_dictionary = {}
    total = 0

    for x in all_categories:
        y = x
        count = 0
        for z in all_categories:
            if (z == y):
                count += 1
        count_dictionary[y] = count

    try:
        del count_dictionary['']
    except(KeyError):
        print("Not enough tweets to analyze precisely")

    list_with_count = [{k: v} for (k, v) in count_dictionary.iteritems()]

    list_with_count = (sorted(list_with_count, key=sort_key, reverse=True))

    count_categories = len(list_with_count)
    print
    print ("Number of distinct categories: ")
    print (count_categories)

    y = 0
    while (y < count_categories):
        temp_category = str(''.join(list_with_count[y].keys()))
        total += sentiment.classify_average(categorized_text[temp_category].encode('utf-8'))
        y += 1

    print
    print ("Average sentiment")
    print (total/count_categories)

    i = -1

    print
    print ("The score depicts the sentiment and the magnitude depicts the amount of emotion")
    print

    while (i < 5):
        i += 1
        if (i == 0):
            try:
                high_category1 = str(''.join(list_with_count[i].keys()))
                print ("1st: " + high_category1)
                sentiment.classify_sentiment(categorized_text[high_category1].encode('utf-8'))
            except(IndexError):
                print ("The tweets weren't long enough to determine categories")
            print
        elif (i == 1):
            try:
                high_category2 = str(''.join(list_with_count[i].keys()))
                print ("2nd: " + high_category2)
                sentiment.classify_sentiment(categorized_text[high_category2].encode('utf-8'))
            except(IndexError):
                break
            print
        elif (i == 2):
            try:
                high_category3 = str(''.join(list_with_count[i].keys()))
                print ("3rd: " + high_category3)
                sentiment.classify_sentiment(categorized_text[high_category3].encode('utf-8'))
            except:
                break
            print
        elif (i == 3):
            try:
                high_category4 = str(''.join(list_with_count[i].keys()))
                print ("4th: " + high_category4)
                sentiment.classify_sentiment(categorized_text[high_category4].encode('utf-8'))
            except:
                break
            print
        elif (i == 4):
            try:
                high_category5 = str(''.join(list_with_count[i].keys()))
                print ("5th: " + high_category5)
                sentiment.classify_sentiment(categorized_text[high_category5].encode('utf-8'))
            except:
                break
            print
