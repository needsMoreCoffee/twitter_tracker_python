import json
import subprocess
import sched, time
from mylogins import twitter

auth_detector_switch = 0
webpage_launch_switch = 0
request_token_switch = 0
session_switch = 0
webpage_launch_switch = 0

def getthatdata(our_session_info):

    params = {  # Include retweets
              'count': 50, # 10 tweets
              'q': '"ufo"',
              'lang': 'en'} #string to search

    #take out session data and PIN from use in authit and grab more JSON, whoot!
    response = our_session_info.get('search/tweets.json', params=params)

    digdata(response)

def get_that_pin(auth_url):
    global auth_detector_switch
    global pin

    #Ensure you only ask for the PIN one time.
    while  auth_detector_switch == 0:

        subprocess.call(["firefox-esr --new-window " + auth_url], shell=True)
        pin = raw_input('Enter PIN from browser: ')  # `input` if using Python 3!
        #switch of fucntions IF statement after authed

        auth_detector_switch += 1
        return pin

    return pin

def get_tokens_and_keep_them():
    global request_token_switch
    global rt
    global rts

    #Only get the tokens once
    while request_token_switch == 0:
        request_token, request_token_secret = twitter.get_request_token()
        rt, rts = request_token, request_token_secret
        request_token_switch += 1
        return rt, rts
    return rt,rts

def authit():
    global session_switch
    global session

    #get the request tokens from get_tokens_and_keep_them
    rt, rts = get_tokens_and_keep_them()
    authorize_url = twitter.get_authorize_url(rt)

    #Get the session informaiton only once using request token and request token secret
    #as well as the PIN
    while session_switch == 0:
        session = twitter.get_auth_session(rt,
                                           rts,
                                           method='POST',
                                           data={'oauth_verifier': get_that_pin(authorize_url)})
        session_switch += 1
        getthatdata(session)
    getthatdata(session)

def digdata(authitdata):
    #Start sorting the data here and loading it into strings that in to the HTML doc
    global webpage_launch_switch
    global combines_datastring
    count = 1
    datastring = []

    for tweet in authitdata.json()['statuses']:
        #This is how we can rid of the retweets.
        if tweet['retweet_count'] == 0:
            #print json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ': '))

            #check that the username doesn't have UFO in the name every other crazy on the new-tab\
            #talking about UFOs does this.
            #check to see if the tweet['retweet_count'] count is over 1 and then skip. Retweets are not
            #going to be valid UFO encounters

            #Now ignore retweets. They couldn't be UFO sightings

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


    #combine everything into one single long string from everything from the loop
    #for each tweet
    combines_datastring = ''.join (str(e) for e in datastring)

    #Writes our webpage HTML to index.html
    webpage(combines_datastring)

    #Open browser or skip if already open
    while webpage_launch_switch == 0:
        openpage()
        webpage_launch_switch += 1

    #Twitter rate limit to 30 second due to TOS
    time.sleep(30)

    #grab our stored session data and then pull some more json
    #and write it to our HTML file
    authit()

def webpage(ourdata):

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

def openpage():
     subprocess.Popen(["firefox-esr --new-tab index.html"], shell=True)

def main():
    authit()

main()
