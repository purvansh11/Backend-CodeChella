#file import of which returns list of cursed tweets
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json
import pickle
import os
import pandas as pd
from pathlib import Path
import tweepy
import re


BASE_DIR = Path(__file__).resolve().parent.parent
Pkl_Filename = os.path.join(BASE_DIR, "myapp/tweet.pkl")
with open(Pkl_Filename, 'rb') as file:  
    Pickled_LR_Model = pickle.load(file)

auth = tweepy.OAuthHandler("9TKAA0gBY5LYuhifr22akTT1t","wTb0FkrvXo4jcRZIiJFvu7Tfb9YSAISmnEHgGVAHC9N6UOMH6M")
auth.set_access_token("1122614380011642881-4ok39qPI31xVLL7j0Oz0vVEAo6xk3d","5b414XzxINpStgxrgqqyHsw58zK3FgqLj3t9xEmXfm3l3")

api = tweepy.API(auth)
userDetails = api.me()
screenname = userDetails.screen_name

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

def getTweet(request):
	if request.method == 'GET':
		cTweets = []
		public_tweets = api.mentions_timeline()
		for tweet in public_tweets:
			y = Pickled_LR_Model.predict(pd.Series(tweet)) 
			if(y == 1):
				cTweets.append(tweet)
		print(tweet.text)

		return JsonResponse(cTweets,state=False)
		#USE FILE HERE TO GET LIST OF SHITTY TWEETS AND RETURN THEM IN RESPONSE



def reportTweet(request):
	if request.method == 'POST': 
		allMentioned = re.findall("/@[A-Za-z0-9_]+/g", request.tweet) #all mentioned tweets
		reportedLists = Diff(allMentioned, list("@"+screenname))

		#except the screenname
		for person in reportedLists:
			api.report_spam(person,request.isblock)
		return JsonResponse(reportedLists,state=False)
      #GET USERNAME/ID FROM REQUEST => CALL THE API TO BLOCK AND REPORT THE USER

def removeTag(request):
	if request.method == 'POST':
		allMentioned = re.findall("/@[A-Za-z0-9_]+/g", request.tweet) #all mentioned tweets
		reportedLists = Diff(allMentioned, list("@"+screenname))
		cleanTweet=""
		for person in reportedLists:
			index = request.tweet.find(person)
			cleanTweet+=request.tweet.substr(index,index+len(person)+1)
		return JsonResponse(cleanTweet,state=False)





	
	


      

      




