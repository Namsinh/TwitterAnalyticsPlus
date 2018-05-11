# This script is similar to test.py, but it is used for the GUI

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


def analyze(username):
    user = api.get_user(username)

    # Initialize a list here

    # Define a function to parse all the information from the list

    # A dictionary for each user's screen name and their tweets
    user_tweets = {}

    count = 0

    print("First, we will analyze tweets of these people you follow")

    for friend in user.friends(count=50):
        # print ("Follower: " + friend.screen_name + "\n")
        # print (friend.screen_name)
        if (count == 0):
            print ("Reading first 5 users right now")
        elif (count % 5 == 0):
            print ("Reading users " + str(count) + " - " + str(count+5) +
                   " right now")
        count += 1
        search = friend.screen_name
        print (search)
        try:
            all_tweets = ""
            tweets = api.user_timeline(
                screen_name=search, count=10, tweet_mode="extended")
            for tweet in tweets:
                all_tweets += tweet.full_text
            try:
                simple_content.simple_classify(all_tweets)
            except(ValueError):
                print ("A friend was skipped due to blocked permissions")

            # Create dictionary with everything
            user_tweets[search] = all_tweets

        except tweepy.TweepError:
            print ("This user has protected tweets. Failed to run")

    return simple_content.print_categories_str()
