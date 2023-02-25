from initSecrets import *
id, api_key = get_aylien_credentials()



import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint

configuration = aylien_news_api.Configuration()
configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = api_key
configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = id

client = aylien_news_api.ApiClient(configuration)
api_instance = aylien_news_api.DefaultApi(client)


args = {
    'id': [123],
    'not_id': [132],
    'story_count_min': 123,
    'story_count_max': 1234,
    'time_start': 'NOW-3DAYS/DAY',
    'time_end': 'NOW-1DAY/DAY',
    'earliest_story_start': 'earliest_story_start_example',
    'earliest_story_end': 'earliest_story_end_example',
    'latest_story_start': 'latest_story_start_example',
    'latest_story_end': 'latest_story_end_example',
    'location_country': ['location_country_example'],
    'not_location_country': ['location_country_example']
}


try:
    api_response = api_instance.list_stories(**args)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_stories: %s\n" % e)



