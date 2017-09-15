import json
import subprocess
import sched, time
from mylogins import twitter


class Twitterbot:
    def __init__(self):
        self.auth_detector_switch = 0
        self.request_token_switch = 0
        self.session_switch = 0

    def getthatdata(self):

        params = {  # Include retweets
                  'count': 50, # 10 tweets
                  'q': '"equifax"',
                  'lang': 'en'} #string to search

        #take out session data and PIN from use in authit and grab more JSON, whoot!
        response = self.session.get('search/tweets.json', params=params)

        return response

    def get_that_pin(self, auth_url):

        while  self.auth_detector_switch == 0:

            subprocess.call(["firefox-esr --new-window " + auth_url], shell=True)
            pin = raw_input('Enter PIN from browser: ')  # `input` if using Python 3!
            self.auth_detector_switch += 1
            return pin

        return pin

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
            if tweet['retweet_count'] == 0:
                #print json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ': '))

                handle = tweet['user']['screen_name']
                retweet = tweet['retweeted']
                retweetcount = tweet['retweet_count']
                text = tweet['text']
                profile_image = tweet['user']['profile_image_url']

                print "screenname is :", tweet['user']['screen_name']
                print "count for retweets", retweetcount
                print "Is this a retweet:", retweet

                profile_image_html = '<img src = "' + profile_image + '" id = "profile_pics"><br>'
                #print profile_image
                #finish builsing the "tweet" structure

                tweets = '<div id = "tweetboxes">' + profile_image_html + str(retweetcount)+  ')' + str(count) + ".) - " + "<b>" + handle + "</b>" + "-" + text + '</div>' + '<br><br>'

                #Encode to ascII
                encodedtweet = [str(unicodes.encode("ascii", "ignore")) for unicodes in tweets]

                #join everything together looks like --> d,d,g,d,s,df,g,..no good. makes a string now
                finishedtweet = ''.join (str(e) for e in encodedtweet)

                datastring.append(finishedtweet)
                count += 1
            else:
                pass

        combines_datastring = ''.join (str(e) for e in datastring)

        return combines_datastring

    def webpage(self, ourdata):

        html_str = '''
        <html>
        <head>
        <LINK REL=StyleSheet HREF="style.css" TYPE="text/css">
        <!-- refreash the page in the browser over and over to load our new data every few minutes-->
        <meta http-equiv="refresh" content="31" >
        </head>
        <body><center><img src="ad-ufora.gif"></img>
        <br>
        <br>
        </center><center><p>{0}</p></center>
        </body>
        </html>'''.format(ourdata)

        htmlfile = open("index.html","w")
        htmlfile.write(html_str)
        htmlfile.close()

    def openpage(self):
         subprocess.Popen(["firefox-esr --new-tab index.html"], shell=True)

mydata = DataThing()

if __name__ == '__main__':

   twit.authit()
   data = twit.getthatdata()
   combined_parsed_data = mydata.digdata(data)
   mydata.webpage(combined_parsed_data)
   mydata.openpage()
