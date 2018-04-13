from __future__ import absolute_import, print_function

import tweepy

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

for friend in user.friends():
    # print ("Follower: " + friend.screen_name + "\n")
    # print (friend.screen_name)
    search = friend.screen_name
    try:
        tweets = api.user_timeline(
            screen_name=search, count=10, tweet_mode="extended")
        full_tweets = [[tweet.full_text] for tweet in tweets]
        # concatenate the contents of each tweet to a new list or something
        print (full_tweets)

    except tweepy.TweepError:
        print ("This user has protected tweets. Failed to run")
