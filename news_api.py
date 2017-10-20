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
        self.api_key = os.environ['NYTIMES_API_KEY']

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


        for i in mydata:
            if 'response' in i:
                for x in i['response']['docs']:
                    if 'pub_date' in x:
                        # print(count)
                        # print(x['pub_date'])
                        newdata['id'] = count
                        newdata['sentiment'] = self.analyser.get_sentiment(x['headline']['main'])
                        time.sleep(.1)
                        newdata['pub_date'] = x['pub_date']
                        newdata['snippet'] = x['snippet']
                        # print(newdata)
                        mylist.append(newdata)
                        # print(newdata)

                    else:
                        print("didn't do anything")
                        pass
            else:
                print("something happened")

        print(mylist)

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

    def test(self, data):

        for i in data:
            if 'response' in i:
                for x in i['response']['docs']:
                    if 'pub_date' in x:
                        sentiment_score = self.analyser.get_sentiment(x['headline']['main'])
                        print("Main Headline: " + x['headline']['main'] + " Published Date: " + str(x['pub_date']) + " Sentiment Rating: " + str(sentiment_score) +
                        " Sentiment: " + str(self.analyser.convertscore(sentiment_score)) + "\n")
                    else:
                        print("didn't do anything")

    def make_dict(self, data):
        count = 0
        newdata = dict()
        mylist = []
        print("newsdfsfss")
        for i in data:
            if 'response' in i:
                for x in i['response']['docs']:
                    if 'pub_date' in x:
                        # print(count)
                        # print(x['pub_date'])
                        newdata['id'] = count
                        count = count + 1
                        newdata['sentiment'] = self.analyser.get_sentiment(x['headline']['main'])
                        newdata['pub_date'] = x['pub_date']
                        newdata['snippet'] = x['snippet']
                        # print(newdata)
                        mylist.append(newdata)
                        # print(newdata)

                    else:
                        print("didn't do anything")
                        pass
            else:
                print("something happened")

        print(mylist)

                    # if 'pub_date' in x:
                    #     print(count)
                    #     print(x['pub_date'])
                    #     data['id'] = count
                    #     count + 1
                    #     data['sentiment'] = self.analyser.get_sentiment(x['headline']['main'])
                    #     data['pub_date'] = x['pub_date']
                    #     # print("Main Headline: " + x['headline']['main'] + " Published Date: " + str(x['pub_date']) + " Sentiment Rating: " + str(sentiment_score) +
                    #     # " Sentiment: " + str(self.analyser.convertscore(sentiment_score)) + "\n")
                    # else:
                    #     print("didn't do anything")


news_thing = Nynews()
