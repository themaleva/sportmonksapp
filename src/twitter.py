import json
from twython import Twython
from .utils import *

with open('./credentials.json', 'r') as creds_file:
    creds = json.load(creds_file)

twitter = Twython(creds['twitter']['CONSUMER_KEY'], creds['twitter']['CONSUMER_SECRET'],
                  creds['twitter']['ACCESS_TOKEN'], creds['twitter']['ACCESS_SECRET'])


def post_tweet(tweet):
    try:
        twitter.update_status(status=tweet)
        add_log(f'TWEETED - {tweet}')
    except:
        add_log(f"### ERROR ### this tweet wasn't posted - Tweet: {tweet}")
    return
