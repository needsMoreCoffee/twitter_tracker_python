import aylien_news_api
from aylien_news_api.rest import ApiException
import os

# Pull our environment vars
aylien_app_id = os.environ["AYLIEN_APP_ID"]
aylien_api_key = os.environ["AYLIEN_API_KEY"]

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = aylien_app_id
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = aylien_api_key

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

text = '"bitcoin" AND "Bitcoin"'
country = ['US']
since = 'NOW-60DAYS/DAY'
until = 'NOW'
sentiment = 'negative'


try:
    # List stories
    api_response = api_instance.list_time_series(text=text, source_locations_country=country, published_at_start=since, published_at_end=until, sentiment_title_polarity = sentiment)
    print(dir(api_response))
    print(api_response.time_series)
    dict = api_response.to_dict

    print(dir(dict))
    # for v,k in dict:
        # print(v, k)

    # for i in api_response:
    #     for k in i:
    #         print k

except ApiException as e:
    print("Exception when calling DefaultApi->list_time_series: %s\n" % e)
