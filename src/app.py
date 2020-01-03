import datetime
import json
from twython import Twython
from twitter import *

with open('./credentials.json', 'r') as creds_file:
    creds = json.load(creds_file)

twitter = Twython(creds['twitter']['CONSUMER_KEY'], creds['twitter']['CONSUMER_SECRET'],
                  creds['twitter']['ACCESS_TOKEN'], creds['twitter']['ACCESS_SECRET'])

soccer_api = f"?api_token={creds['sportmonks']['TOKEN']}"

# Set various date variables & formats
today = datetime.datetime.now()  # Raw date
todays_date = today.strftime('%Y') + '-' + today.strftime('%m') + '-' + today.strftime('%d')  # YYYY-MM-DD Format
check_date = today.strftime('%d') + '-' + today.strftime('%B') + '-' + today.strftime('%Y')  # DD-MMM-YYYY Format
