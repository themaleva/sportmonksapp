import datetime
import json
from twitter import *
from sportmonks import *

with open('./config.json') as config_file:
    config = json.load(config_file)

soccer_api = f"?api_token={creds['sportmonks']['TOKEN']}"

# Set various date variables & formats
today = datetime.datetime.now()  # Raw date
todays_date = today.strftime('%Y') + '-' + today.strftime('%m') + '-' + today.strftime('%d')  # YYYY-MM-DD Format
check_date = today.strftime('%d') + '-' + today.strftime('%B') + '-' + today.strftime('%Y')  # DD-MMM-YYYY Format

endpoint = config['fixtures_url'] + "2019-12-27" + soccer_api + config['fixture_includes']

# get new fixtures from endpoint and only return those from specific league id
fixtures = get_new_fixtures(endpoint, config['league_id'], check_date)

# if new fixtures exists then format the returned dictionary ready to tweet
if fixtures:
    f = format_fixtures_for_twitter(fixtures)
    # tweet today's fixtures
    post_tweet(f)
else:
    pass