import datetime
import json
from twitter import *
from sportmonks import *
from utils import *

with open('./config.json') as config_file:
    config = json.load(config_file)

soccer_api = f"?api_token={creds['sportmonks']['TOKEN']}"


if __name__ == '__main__':

    new_fixtures_endpoint = f"{config['fixtures_url']}{date_today()}{soccer_api}{config['fixture_includes']}"
    test_fixtures_endpoint = f"{config['fixtures_url']}{'2019-12-26'}{soccer_api}{config['fixture_includes']}"
    get_events_endpoint = f"{config['livescores_url']}{soccer_api}{config['livescores_includes']}"
    test_get_event_fixture = f"GET https://soccer.sportmonks.com/api/v2.0/fixtures/11879660/{soccer_api}{config['livescores_includes']}"

    print(test_fixtures_endpoint)

    # get new fixtures from endpoint and only return those from specific league id
    fixtures = get_new_fixtures(test_fixtures_endpoint, config['league_id'], check_date())

    # if new fixtures exists then format the returned dictionary ready to tweet
    if fixtures:
        f = format_fixtures_for_twitter(fixtures)
        # TODO: Uncomment below
        # post_tweet(f) # tweet today's fixtures
        kickoffs = get_kickoffs(fixtures) # get kick-off times from today's matches
        # TODO: Uncomment below
        # time_to_sleep(kickoffs.pop(0))) # calculate sleep time until 1st kickoff

        processed_events = []

        # While all games haven't finished, check for new events
        while all_games_finished(get_events(get_events_endpoint)):

            with open('./test_livescores.json') as file:
                live_events = json.load(file)

            #live_events = get_events(get_events_endpoint)
            new_events, processed_events = process_events(live_events, processed_events)

            print(new_events)

            for event in new_events:
                # post_tweet(event['tweet'])
                # build tweet string
                tweet_str = f''

    else:
        pass
        # TODO: Uncomment below
        # time_to_sleep("06:00"))
