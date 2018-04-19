from google.cloud import language

import os
### Change this path to your local cred.json location ###
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/rabahhabiss/Downloads/TPlus/TwitterAnalyticsPlus/cred.json"


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

classify("Matt Forte, Devin Hester to sign one-day contracts, retire as Chicago Bears. Joel Embiid is listed as doubtful for Game 3 of the Heat-Sixers series on Thursday. Breaking: The Nevada State Athletic Commission has reached an agreement with Canelo Alvarez that will result in a 6-month suspension.")
