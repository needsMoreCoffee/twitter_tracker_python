from rauth import OAuth1Service

twitter = OAuth1Service(
    name = 'twitter',
    consumer_key = 'y9Pr4XY7TbbATjvnByRsYCs4A',
    consumer_secret = '9nxeN7nqPEamlUl7wRicAdxbi47tI7vMuLMoGvW2nKCTfuHHfY',
    request_token_url = 'https://api.twitter.com/oauth/request_token',
    access_token_url = 'https://api.twitter.com/oauth/access_token',
    authorize_url = 'https://api.twitter.com/oauth/authorize',
    base_url = 'https://api.twitter.com/1.1/')
