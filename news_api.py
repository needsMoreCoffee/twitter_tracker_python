import urllib
import urllib2
import json
import time
import os
from sentiment_thing import Analysis


class Nynews:
    def __init__(self):
        self.fl_params = "headline,pub_date,snippet"
        self.search_query = "bitcoin"
        self.data = []
        self.page = 5
        self.analyser = Analysis()
        self.api_key = os.environ['NYTIMES_API_KEY']

    def get_data(self):
        mydata = []
        print("pullng data")
        for i in range(self.page):
            response = urllib2.urlopen("http://api.nytimes.com/svc/search/v2/articlesearch.json?fl=%s&q=%s&page=%s&api-key=%s" % ( self.fl_params, self.search_query, i, self.api_key))
            mydata.append(json.load(response))
            time.sleep(5.1)
        print(type(mydata))
        return mydata

    def look_at_data(self, data):

        for i in data:
            if 'response' in i:
                for x in i['response']['docs']:
                    if 'pub_date' in x:
                        sentiment_score = self.analyser.get_sentiment(x['headline']['main'])
                        print("Main Headline: " + x['headline']['main'] + " Published Date: " + str(x['pub_date']) + " Sentiment Rating: " + str(sentiment_score) +
                        " Sentiment: " + str(self.analyser.convertscore(sentiment_score)) + "\n")
                    else:
                        print("didn't do anything")

news_thing = Nynews()
