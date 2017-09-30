import json
import subprocess
import sched, time
from mylogins import twitter
from sentiment_thing import *


class Twitterbot:
    def __init__(self):
        self.auth_detector_switch = 0
        self.request_token_switch = 0
        self.session_switch = 0

    def getthatdata(self):

        params = {  # Include retweets
                  'count': 100, # 10 tweets
                  'q': '"equifax"',
                  'result_type': 'recent',
                  'lang': 'en'} #string to search

        #take out session data and PIN from use in authit and grab more JSON, whoot!
        response = self.session.get('search/tweets.json', params=params)

        return response

    def get_that_pin(self, auth_url):

        while  self.auth_detector_switch == 0:

            subprocess.call(["firefox-esr --new-window " + auth_url], shell=True)
            self.pin = raw_input('Enter PIN from browser: ')  # `input` if using Python 3!
            self.auth_detector_switch += 1
            return self.pin

        return self.pin

    def get_tokens_and_keep_them(self):

        while self.request_token_switch == 0:
            request_token, request_token_secret = twitter.get_request_token()
            rt, rts = request_token, request_token_secret
            self.request_token_switch += 1
            return rt, rts
        return rt,rts

    def authit(self):

        rt, rts = self.get_tokens_and_keep_them()
        authorize_url = twitter.get_authorize_url(rt)

        #Get the session informaiton only once using request token and request token secret
        while self.session_switch == 0:
            self.session = twitter.get_auth_session(rt,
                                               rts,
                                               method='POST',
                                               data={'oauth_verifier': self.get_that_pin(authorize_url)})
            self.session_switch += 1

twit = Twitterbot()

class DataThing:
    def __init__(self):
        self.webpage_launch_switch = 0
        self.combines_datastring = []

    def digdata(self, authitdata):
        #Start sorting the data here and loading it into strings that in to the HTML doc
        count = 1
        datastring = []

        for tweet in authitdata.json()['statuses']:
            #This is how we can rid of the retweets.
            print(tweet)
            if tweet['retweet_count'] == 0:
                #print json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ': '))

                handle = tweet['user']['screen_name']
                retweet = tweet['retweeted']
                retweetcount = tweet['retweet_count']
                text = tweet['text']
                profile_image = tweet['user']['profile_image_url']

                # print(text)

                # print "screenname is :", tweet['user']['screen_name']

                # tweets = '<div id = "tweetboxes">' + profile_image_html + str(retweetcount)+  ')' + str(count) + ".) - " + "<b>" + handle + "</b>" + "-" + text + '</div>' + '<br><br>'

                #Encode to ascII
                # encodedtweet = [str(unicodes.encode("ascii", "ignore")) for unicodes in text]
                # print(encodedtweet)

                #join everything together looks like --> d,d,g,d,s,df,g,..no good. makes a string now

                # datastring.append(finishedtweet)

                # finishedtweet = ''.join(str(e) for e in encodedtweet)
                datastring.append(text)
                count += 1

            else:
                pass

        # combines_datastring = ''.join(str(e) for e in datastring)

        return datastring

mydata = DataThing()

if __name__ == '__main__':
    arr =[]
    twit.authit()
    data = twit.getthatdata()
    combined_parsed_data = mydata.digdata(data)
    analyser = Analysis()
    count = 1
    for i in combined_parsed_data:
        print(str(count) + i + ' : ' + 'Sentiment Rating: ' + str(analyser.get_sentiment(i)))
        arr.append(analyser.get_sentiment(i))
        count + 1
    print("-------------------------------------")
    print(arr)
   # mydata.webpage(combined_parsed_data)
   # mydata.openpage()
