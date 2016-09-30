import json
import subprocess
import sched, time
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
    tweetdata
    return tweetdata


def digdata(authitdata):
#Start sorting the data here and loading it into strings
    count = 1
    datastring = []
    for tweet in authitdata.json()['statuses']:

        handle = tweet['user']['screen_name']
        text = tweet['text']

        #finish builsing the "tweet" structure
        tweets = '<div id = "tweetboxes">' + str(count) + ".) - " + handle + "-" + text + '</div>' + '<br>'
        #decode to ascII
        encodedtweet = [str(unicodes.encode("ascii", "ignore")) for unicodes in tweets]
        #join everything together looks like --> d,d,g,d,s,df,g,..no good. makes a string now
        finishedtweet = ''.join (str(e) for e in encodedtweet)

        datastring.append(finishedtweet)

        count = count + 1
    #combine everything into one single long string from everything from the loop
    combines_datastring = ''.join (str(e) for e in datastring)

    webpage(combines_datastring)


def webpage(ourdata):

    html_str = '''
    <html>
    <head>
    <LINK REL=StyleSheet HREF="style.css" TYPE="text/css">
    <!-- refreash the page in the browser over and over to load our new data every few minutes-->
    <meta http-equiv="refresh" content="10" >
    </head>
    <body><center><img src="ad-ufora.gif"></img>
    <br>
    <br>
    </center><center><p>{0}</p></center>
    </body>
    </html>'''.format(ourdata)

    #print html_str

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
     subprocess.Popen(["firefox-esr --new-tab index.html"], shell=True)

def main():
    authit()

main()
