import os
import json
import glob
import requests
import oauth2 as oauth
from requests_oauthlib import OAuth1
API_KEY = "jMvh5z8BFJRI1DKddAxM6OZvO"
API_SECRET = "6sprlWMLZr4loaJsCjX9jEejnwZ9IVSLu2ZfVRoUayHzfdeWSI"
ACCESS_TOKEN = "787049875414388736-qG5LXieK4WbMfQh2mjF1dMHrOhc24F7"
ACCESS_TOKEN_SECRET = "zl8znYFwQSKSrfH8QT2v4pAi8kLDPiLlLb5zzTyeuZ1kK"



oauth = OAuth1(API_KEY,  
         API_SECRET,  
         ACCESS_TOKEN,  
         ACCESS_TOKEN_SECRET)  

r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=AkshayKumar", auth=oauth) 
a = r.json()
myStatuses = a['statuses']

count=
text = None
for j in myStatuses:
    myTweets = j['followers_count']
    if myTweets > count:
        count = myTweets
        text = j['text']
		print(count)
		print(text)
        
    
