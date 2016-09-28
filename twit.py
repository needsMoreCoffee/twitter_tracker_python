import json
import subprocess
from mylogins import twitter

#see mylogins.py for the data needed to get this working will follow the
#following format.
# from rauth import OAuth1Service
#twitter = OAuth1Service(
#    name = 'twitter',
#    consumer_key = '',
#    consumer_secret = '',
#    request_token_url = 'https://api.twitter.com/oauth/request_token',
#    access_token_url = 'https://api.twitter.com/oauth/access_token',
#    authorize_url = 'https://api.twitter.com/oauth/authorize',
#    base_url = 'https://api.twitter.com/1.1/')

def authit():
# check if all ready authed and then ask for pin if not otherwise get more authed data.
    pin = 0
    if pin == 0:
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

    else:
        r = session.get('search/tweets.json', params=params)

    digdata(r)

def killunicode(tweetdata):
    tweetdata = [str(unicodes.encode("ascii", "ignore")) for unicodes in tweetdata]
    return tweetdata


def digdata(authitdata):
#Start sorting the data here and loading it into strings
    count = 1
    for tweet in authitdata.json()['statuses']:
        #handle = tweet['user']['screen_name']
        #text = tweet['text']
        encodedtweet = killunicode(tweet)
        tweets = count, ')' + encodedtweet['user']['screen_name'] + ' - ' + encodedtweet['text'] + "<br>"
        datastring = []
        datastring.append(tweets)
        count = count + 1
        #print count, ')' + tweet['user']['screen_name'] + ' - ' + tweet['text']
        #print '\n'
    webpage(datastring)


def webpage(ourdata):

    html_str = '''
    <html>
    <head>
    <!-- refreash the page in the browser over and over to load our new data every few minutes-->
    <meta http-equiv="refresh" content="10" >
    </head>
    <body>''' + '<center><img src="ad-ufora.gif"></img></center>' + "<center><p>" + str(ourdata) + "</p></center>" + '</body> </html>'

    htmlfile = open("index.html","w")
    htmlfile.write(html_str)
    htmlfile.close()

# check to see if the webpage has been opened in a
# browser first otherwise skip it
    init_open_counter = 0

    if init_open_counter <= 0:
        init_open_counter += 1
        openpage()
    else:
        pass

def openpage():
     subprocess.call(["firefox-esr --new-tab" + "index.html"], shell=True)

def main():
    authit()

main()
