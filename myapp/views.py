#file import of which returns list of cursed tweets
from django.shortcuts import render, HttpResponse
import json

def getTweet(request):
   if request.method == 'GET': 
      return HttpResponse("wdad")
      #USE FILE HERE TO GET LIST OF SHITTY TWEETS AND RETURN THEM IN RESPONSE



def reportTweet(request):
   if request.method == 'POST': 
      return HttpResponse("asfafa")
      #GET USERNAME/ID FROM REQUEST => CALL THE API TO BLOCK AND REPORT THE USER




      

      




