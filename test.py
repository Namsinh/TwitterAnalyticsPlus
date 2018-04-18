from __future__ import absolute_import, print_function

import tweepy
import simple_content

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key = 'HbZtZIbWlAlDmrDyKgcssTBZY'
consumer_secret = 'VQr0r3LaETOmJWJ4VZxco7lwWIq2RuXy4uLXD0WRHdAWaXbwSH'

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token = '983388258288599040-kxqW9IFDEclkqTMh5CNXduOGBEU5AU2'
access_token_secret = 'HKIkCdrAaJ6cMxEmqIEvBgWdwDecEq7Uv97E6dpAbiRTl'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user('data_cu')

print ()
print ("****** Testing the twitter anaylytics platform ********")
print ()

# Initialize a list here

# Define a function to parse all the information from the list

# A dictionary for each user's screen name and their tweets
user_tweets = {}

for friend in user.friends():
    # print ("Follower: " + friend.screen_name + "\n")
    # print (friend.screen_name)
    search = friend.screen_name
    try:
        all_tweets = ""
        tweets = api.user_timeline(
            screen_name=search, count=1, tweet_mode="extended")
        for tweet in tweets:
            all_tweets += tweet.full_text
        print (search)
        try:
            print ("Here is the classification")
            simple_content.classify(all_tweets)
        except:
            print ("Error. The probably language is not supported")

        # Create dictionary with everything
        user_tweets[search] = all_tweets

    except tweepy.TweepError:
        print ("This user has protected tweets. Failed to run")

# print (user_tweets)
