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
        self.page = 2
        self.analyser = Analysis()
        self.api_key = 'put_your_key_here'
        # self.api_key = os.environ['NYTIMES_API_KEY']

    def get_data(self):
        mydata = []
        count = 0
        newdata = dict()
        mylist = []

        print("pullng data")
        for i in range(self.page):
            response = urllib2.urlopen("http://api.nytimes.com/svc/search/v2/articlesearch.json?fl=%s&q=%s&page=%s&api-key=%s" % ( self.fl_params, self.search_query, i, self.api_key))
            mydata.append(json.load(response))
            time.sleep(1.1)


        for q in mydata:
            for x in q['response']['docs']:
                if 'pub_date' in x:
                    mylist.append(dict())
                    mylist[count]['id'] = count
                    mylist[count]['pub_date'] = x['pub_date']
                    mylist[count]['snippet'] = x['snippet']
                    count = count + 1
                else:
                    print("no response ? ")

        return mylist

    def look_at_data(self, data):

        for i in data:
            print i

    def add_sentiment(self, data):

        for i in data:
            i['sentiment'] = self.analyser.get_sentiment(i['snippet'])
            print(i['sentiment'])

        return data

newsthingy = Nynews()
