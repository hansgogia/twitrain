import webbrowser
import sys
import tweepy
import os
import bz2

consumer_key = 'werVqzTQcXHlJtgwCwtqxA'
consumer_secret = 'cDosDXtGMPcVZugpPcD3Z8jhIEOwiOHgqd9Hmd4QMk'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
filename = ".twitrain_oauth"

if os.path.exists(filename) == True:
    oauth = open(filename , 'r')
    decode = oauth.readline()
    a = decode.split('&')
    k = a[0]
    s = a[1]
else:
    webbrowser.open(auth.get_authorization_url())
    verifier = raw_input('enter pin :\n')
    token = auth.get_access_token(verifier)
    oauth_file = open(filename,'w')
    oauth_file.write(str(token.key))
    oauth_file.write('&')
    oauth_file.write(str(token.secret))
    oauth_file.close()
    k = token.key
    s = token.secret

auth.set_access_token(k,s)
api = tweepy.API(auth)
