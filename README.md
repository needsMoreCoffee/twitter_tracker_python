# Market Sentiment Machine

## Work in Progress

The Market Sentiment Machine will test the news and twitter messages to get headline and tweet sentiment on a company or a crypo currency. Using sentiment and finance data we will test how much market sentiment will drive the market.  

In the current condition this is more of a personal toolkit. 

The develop branch is a version of this that looks for 'UFO' text and charts the tweets on a webpage with location to start testing the idea that mass sightings can be tracked online no matter if its a 'UFO' sighting, crime in progress, or other.

**currently being developed. More of a toolkit in its current state**

This application samples tweets from the twitter sphere and detects sentiment of the users tweets. Used to track a companies online "market sentiment".

# Motivation

My motivation is to see if there is a correlation between sentiment on twitter and the stock market.

# How To Run

Download and navigate into the scripts directory and then run python twit.py

# Modules

json

subprocess

mylogins.py

twitter

google.cloud

## Mylogin.py File Below - Fill Out The Information From Your Account.

```
# from rauth import OAuth1Service
#twitter = OAuth1Service(
#    name = 'twitter',
#    consumer_key = '',
#    consumer_secret = '',
#    request_token_url = 'https://api.twitter.com/oauth/request_token',
#    access_token_url = 'https://api.twitter.com/oauth/access_token',
#    authorize_url = 'https://api.twitter.com/oauth/authorize',
#    base_url = 'https://api.twitter.com/1.1/')

```

## Follow Googles Instructions For Setting Up The Sentiment api

```
https://cloud.google.com/natural-language/docs/getting-started#set_up_your_project

```
