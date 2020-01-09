import requests
import json
from utils import *


# Check for new fixtures
def get_new_fixtures(endpoint, league_id, date):
    add_log(f'Beginning check for new fixtures on {date}')
    raw_fixtures = json.loads(requests.get(endpoint).content)
    add_log(f'Completed check for new fixtures on {date}')

    if not raw_fixtures['data']:
        add_log(f'No fixtures scheduled today ({date})')
        return 0

    else:
        fixtures = {}
        for f in raw_fixtures['data']:
            # make sure the fixtures are in the specified league before adding to our dictionary
            if f['league_id'] == league_id:
                fixture = f['localTeam']['data']['name'] + ' vs ' + f['visitorTeam']['data']['name']
                fixtures[fixture] = {'id': f['id'], 'start_time': f['time']['starting_at']['time']}
            else:
                pass

    return fixtures


def format_fixtures_for_twitter(fixtures):
    fixture_list = "Today's Fixtures:\n\n"
    for key in fixtures.keys():
        fixture_list += f'{key} ({fixtures[key]["start_time"]})\n'
    return fixture_list


def get_kickoffs(fixtures):
    # get stored fixtures from today's file

    kick_offs = []

    for fixture in fixtures:
        ko_time = (fixtures[fixture]['start_time'])
        if ko_time in kick_offs:
            pass
        else:
            kick_offs.append(ko_time)

    sorted(kick_offs)

    return kick_offs


def get_events(endpoint):
    add_log('Checking for live updates')  # logging

    livescore_data = json.loads(requests.get(endpoint).content)

    return livescore_data


def check_all_games_ft(matches):
    total_matches = len(matches['data'])
    completed_matches = 0
    for match in matches['data']:
        if match['time']['status'] == 'FT':
            completed_matches += 1
        else:
            pass

    if total_matches == completed_matches:
        return True
    else:
        return False


def process_events(matches):
    events = []
    # for match in matches['data']:
    #     for event in match['events']['data']:
    #         if event['type'] == 'goal':

    return events


def tweet_events(events):

    for event in events:


