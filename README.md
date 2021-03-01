# Market Sentiment Toolkit - Searching terms in Tweet and News data and testing for language sentiment using NLP

The Market Sentiment Machine will test the news and twitter messages to get headline and tweet sentiment on a company or a crypo currency. Using sentiment and finance data we will test how sentiment will drive the stock prices up and down. 

This application samples tweets and news sources and detects sentiment of the users tweets. Used to track a companies online "market sentiment".

## Motivation

My motivation is to see if there is a correlation between sentiment on twitter or news and the stock market.

# How To Run The Tools

**market_data.py** - Run this script to chart your stock for the day. 

**news_sentiment_time_series.py** - This script is used to do in depth research on on many news articles at once and their sentiment. This is close to what isa offered in their stock API docs, but i included here because it is a great resource for watching your stock and picking up on buy/sell sentiment

**news_api.py** This pulls small snippets or highlight from news articles at NYTimes and then runs through Google NLP sentiment analysis. 

**Twit.py** - This will search recent Twitter data looking for tweets about your search terms and run through Google NLP sentiment analysis. 

**sentiment_thing.py** - twit.py and news_api.py both use this imported to process and return sentiment. Use on your own text if you like.

## Modules

json

matplotlib

python-tk

pandas_datareader

subprocess

mylogins.py

twitter

google.cloud

## Install the following

apt-get install python-tk

### Make the file call Mylogin.py 

Fill Out The Information From Your twitter Account for twit.py

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
