import datetime
import json
from twitter import *
from sportmonks import *
from utils import *

with open('./config.json') as config_file:
    config = json.load(config_file)

soccer_api = f"?api_token={creds['sportmonks']['TOKEN']}"


class Runner:
    def __init__(self):
        self.date = datetime.datetime.now()

    def date_today(self):  # YYYY-MM-DD Format
        date_today = self.date.strftime('%Y') + '-' + self.date.strftime('%m') + '-' + self.date.strftime('%d')
        return date_today

    def check_date(self):  # DD-MMM-YYYY Format
        check_date = self.date.strftime('%d') + '-' + self.date.strftime('%B') + '-' + self.date.strftime('%Y')
        return check_date


if __name__ == '__main__':

    while True:

        new_run = Runner()

        new_fixtures_endpoint = f"{config['fixtures_url']}{new_run.date_today()}{soccer_api}{config['fixture_includes']}"
        get_events_endpoint = f"{config['livescores_url']}{soccer_api}{config['livescores_includes']}"

        # get new fixtures from endpoint and only return those from specific league id
        fixtures = get_new_fixtures(new_fixtures_endpoint, config['league_id'], new_run.check_date)

        # if new fixtures exists then format the returned dictionary ready to tweet
        if fixtures:
            f = format_fixtures_for_twitter(fixtures)
            # tweet today's fixtures
            post_tweet(f)
        else:
            print(time_to_sleep("06:00"))
