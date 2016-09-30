import json
import subprocess
import sched, time
from mylogins import twitter

auth_detector_switch = 0
webpage_launch_switch = 0
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

def getthatdata(our_session_info):

    params = {  # Include retweets
              'count': 10, # 10 tweets
              'q': '"ufo"',
              'lang': 'en'} #string to search

    #take out session data and PIN from use in authit and grab more JSON, whoot!
    r = our_session_info.get('search/tweets.json', params=params)

    digdata(r)

def authit():
# check if all ready authed and then ask for pin if not otherwise get more authed data.
    global auth_detector_switch

    # do not run the auth process if already done.
    if  auth_detector_switch == 0:

        request_token, request_token_secret = twitter.get_request_token()
        authorize_url = twitter.get_authorize_url(request_token)

        params = {  # Include retweets
                  'count': 10, # 10 tweets
                  'q': '"ufo"',
                  'lang': 'en'} #string to search

        print 'Visit this URL in your browser: ' + authorize_url
        #This opens firefox-esr new window for the PIN code
        subprocess.call(["firefox-esr --new-window " + authorize_url], shell=True)
        pin = raw_input('Enter PIN from browser: ')  # `input` if using Python 3!

        session = twitter.get_auth_session(request_token,
                                request_token_secret,
                                method='POST',
                                data={'oauth_verifier': pin})
        #switch of fucntions IF statement after authed
        auth_detector_switch += 1

        getthatdata(session)


def digdata(authitdata):
#Start sorting the data here and loading it into strings
    global webpage_launch_switch
    count = 0
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
        count += 1
    #combine everything into one single long string from everything from the loop
    combines_datastring = ''.join (str(e) for e in datastring)

    #Skip opening page if already open
    if webpage_launch_switch == 0:
        webpage(combines_datastring)
        webpage_launch_switch += 1

    #keep passing the session info to the twitter API and rewrite the HTML
    time.sleep(10)
    authit()

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

def openpage():
     subprocess.Popen(["firefox-esr --new-tab index.html"], shell=True)

def main():
    authit()

main()
