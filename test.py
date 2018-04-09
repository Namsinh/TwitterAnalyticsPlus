from __future__ import absolute_import, print_function

import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key = '######'
consumer_secret = '######'

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token = '######'
access_token_secret = '#####'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user('data_cu')

for friend in user.followers():
    print ("First followers tweets!! \n\n")
    print (friend.screen_name)
    search = friend.screen_name
    tweets = api.user_timeline(screen_name=search, count=1, include_rts=True)
    for status in tweets:
        print (status.text)
