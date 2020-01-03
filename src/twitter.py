from utils import *


def post_tweet(twitter, tweet):
    try:
        twitter.update_status(status=tweet)
        add_log(f'TWEETED - {tweet}')
    except:
        add_log(f"### ERROR ### this tweet wasn't posted - Tweet: {tweet}")
    return()