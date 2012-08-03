import android
import sys
import tweepy
import os

droid = android.Android()
consumer_key = 'ENTER CONSUMER KEY HERE'
consumer_secret = 'ENTER CONSUMER SECRET HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token('ENTER TOKEN KEY HERE','ENTER TOKEN SECRET HERE') #This is a static login. Look out later for further updates.
api = tweepy.API(auth)
