from __future__ import absolute_import, print_function
import json
import tweepy
import tokenizer

#
# Description: This script does the following:
#               * Connects to Twitter's API
#               * Retrieves the most recent tweets of a username provided by the user
#               * Stores the tweets in a json file
#               * Prints the contents of a json file
#               * Pre-processes the text content in a json file
# Dependencies: Tweepy, NLTK
#


# == Twitter OAuth Authentication ==
consumer_key = 'HbZtZIbWlAlDmrDyKgcssTBZY'
consumer_secret = 'VQr0r3LaETOmJWJ4VZxco7lwWIq2RuXy4uLXD0WRHdAWaXbwSH'

# Twitter Access Token
access_token = '983388258288599040-kxqW9IFDEclkqTMh5CNXduOGBEU5AU2'
access_token_secret = 'HKIkCdrAaJ6cMxEmqIEvBgWdwDecEq7Uv97E6dpAbiRTl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# print json
def print_json(filename):
    with open('tweets.json', 'r') as f:
        line = f.readline() #read only the first tweet
        tweet = json.loads(line) #load it as python dict
        print(json.dumps(tweet, indent=4)) # pretty-print

#print_json("tweets.json")

# store json
def store_json(tweet):
    with open('tweets.json', 'w') as fp:
        json.dump(tweet, fp)
        print(json.dumps(tweet))

# text preprocessing
def preprocess_tweets(json_file):
    with open(json_file, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            tokens = tokenizer.preprocess(tweet['text'])
            print(tokens)


    
# I/O Placeholder
username = input('Username on Twitter (public accounts only): ')

# Getting the tweet json object 
try:
    for tweet in tweepy.Cursor(api.user_timeline, id=username).items(10):
        store_json(tweet._json)

except tweepy.TweepError:
    print ("This user has protected tweets. Failed to run")

# Preprocessing the text in the tweet object
preprocess_tweets('tweets.json')

