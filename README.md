# Twitter Analytics+

This application aims to provide the user with insights on the nature of content being published by the people they follow.

The application is still in the development stage.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Setting up the environment

The following dependencies must be installed in your machine in order to compile the application:

* Python 2.4.0+
* <a href="https://github.com/tweepy/tweepy/" target="_blank">Tweepy</a>: A Python library for accessing Twitter API
> To install Tweepy package using pip run the following command in your terminal:

```
$ pip install tweepy
```

* Google Cloud Natural Language
> To install Google Cloud Language run the following command in your terminal:
```
$ pip install --upgrade google-cloud-language
```
A personal access key for Google Services must be obtained.

Further instructions on how to install Google Cloud Language library and set up an access key visit can be found at https://cloud.google.com/natural-language/docs/reference/libraries#client-libraries-install-php

* <a href="http://www.nltk.org">Natural Language Toolkit</a>: To install the package run the following command in the terminal:
```
$ sudo pip install -U nltk
```

### Running and testing the application

The following scripts can be tested by running the files in Python:
* Twitter API connectivety: `./test.py` asks the user to enter a public twitter account, connects to Twitter API and grabs the 10 most recent tweets from accounts in the following list.

* Text Preprocessing: `./tweet_preprocessing.py` stores and retrieves tweet objects in JSON format, and pre-processes the tweets before passing them to Google Cloud.

* Sentiment Analysis: `./sentiment.py`

* Content Classification: `./content.py`
