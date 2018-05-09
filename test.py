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

# I/O Placeholder
print("This tool will help you analyze a public account on twitter based on the accounts they follow.")
name = raw_input('Username on Twitter(public accounts only): ')

user = api.get_user(name)

my_screen_name = user.screen_name
print(my_screen_name)

print ()
print ("****** Testing the twitter anaylytics platform ********")
print ()

print ("First, let's see the categories you tweet about most")
print ()

my_tweets = ""
personal_tweets = api.user_timeline(screen_name=my_screen_name, count=20, tweet_mode="extended")
for x in personal_tweets:
    # print (x.full_text)
    my_tweets += x.full_text
try:
    simple_content.simple_classify(my_tweets)
except:
    print("Language not supported by Google Cloud")

simple_content.print_categories()

# Initialize a list here

# Define a function to parse all the information from the list

# A dictionary for each user's screen name and their tweets
user_tweets = {}

count = 0

print("First, we will analyze the tweets of the following people you follow")

for friend in user.friends(count=50):
    # print ("Follower: " + friend.screen_name + "\n")
    # print (friend.screen_name)
    if (count == 0):
        print ("Reading first 5 users right now")
    elif (count % 5 == 0):
        print ("Reading users " + str(count) + " - " + str(count+5) + " right now")
    count += 1
    search = friend.screen_name
    print (search)
    try:
        all_tweets = ""
        tweets = api.user_timeline(
            screen_name=search, count=1, tweet_mode="extended")
        for tweet in tweets:
            all_tweets += tweet.full_text
        try:
            simple_content.simple_classify(all_tweets)
        except:
            print ("A friend was skipped due to blocked permissions")

        # Create dictionary with everything
        user_tweets[search] = all_tweets

    except tweepy.TweepError:
        print ("This user has protected tweets. Failed to run")


simple_content.print_categories()
