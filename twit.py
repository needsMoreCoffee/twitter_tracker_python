from rauth import OAuth1Service
import json
import subprocess
from mylogins import *
#from mylogins import *

#see mylogins.py for the data needed to get this working will follow the
#following format.

#twitter = OAuth1Service(
#    name = 'twitter',
#    consumer_key = '',
#    consumer_secret = '',
#    request_token_url = 'https://api.twitter.com/oauth/request_token',
#    access_token_url = 'https://api.twitter.com/oauth/access_token',
#    authorize_url = 'https://api.twitter.com/oauth/authorize',
#    base_url = 'https://api.twitter.com/1.1/')

request_token, request_token_secret = twitter.get_request_token()
authorize_url = twitter.get_authorize_url(request_token)

print 'Visit this URL in your browser: ' + authorize_url

#This opens firefox-esr new window for the PIN code
subprocess.call(["firefox-esr --new-window " + authorize_url], shell=True)
pin = raw_input('Enter PIN from browser: ')  # `input` if using Python 3!

session = twitter.get_auth_session(request_token,
                                   request_token_secret,
                                   method='POST',
                                   data={'oauth_verifier': pin})

params = {  # Include retweets
          'count': 10, # 10 tweets
          'q': '"ufo"',
          'lang': 'en'} #string to search

r = session.get('search/tweets.json', params=params)
#print r.json n

# ?q=ufo&result_type=recent
#decoded = json.loads(r)
count = 1
for tweet in r.json()['statuses']:
    #handle = tweet['user']['screen_name']
    #text = tweet['text']
    print count, ')' + tweet['user']['screen_name'] + ' - ' + tweet['text']
    print '\n'
    count = count + 1

#this function writes our returned data into a HTML file to be displayed
def webpage():
    html_str = """
    <html>
     <head>
     <!-- refreash the page in the browser -->
     <meta http-equiv="refresh" content="3" >
     </head>
     <body>

     </body>
     </html>
     """

     Html_file= open("index.html","w")
     Html_file.write(html_str)
     Html_file.close()

     subprocess.call(["firefox-esr --new-tab" + index.html], shell=True)
