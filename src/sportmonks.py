import requests
import json
from .utils import *


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


def all_games_finished(matches):
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


def process_events(matches, processed):

    # Parse all events and pull out the goal events
    # events = [event for match in matches['data'] for event in match['events']['data'] if event['type'] == 'goal']

    events = {}

    for match in matches['data']:
        goals = {}
        for event in match['events']['data']:
            events[match['id']] = {}

            # Add team info to events dictionary
            events[match['id']]['teams'] = {'data': {match['localTeam']['data']['id']: match['localTeam']['data']['name'],
                                             match['visitorTeam']['data']['id']: match['visitorTeam']['data']['name']
                                                     }
                                            }

            # If event is a goal and hasn't already been processed then add to dictionary
            if event['type'] == 'goal' and event['id'] not in processed:

                goals[event['id']] = {'score': event['result'],
                                      'minute': event['minute'],
                                      'scorer': event['player_name'],
                                      'assist_by': event['related_player_name'],
                                      'team_id': event['team_id'],
                                      'tweet': "" # TODO: Figure out how to pull together the right info for this
                                      }

            # Add goals dict to main events dict
            events[match['id']]['goals'] = {'data': goals}

    return events, processed


def tweet_events(events):

    # for event in events:

    return