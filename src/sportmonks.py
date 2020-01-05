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


def get_events(endpoint):
    add_log('checking for live updates')  # logging
    url = livescores_url + soccer_api + livescores_includes

    # get stored fixtures from today's file
    todays_fixtures = get_fixtures()
    first_kickoff = []

    for fixture in todays_fixtures:
        ko_time = (todays_fixtures[fixture]['start_time'])
        if ko_time in first_kickoff:
            pass
        else:
            first_kickoff.append(ko_time)

    first_kickoff.sort()
    next_kickoff = first_kickoff.pop()

    current_time = datetime.datetime.today()

    current_hour = (int(current_time.hour))
    ko_hour = (int(next_kickoff[0:2]))
    current_min = (int(current_time.minute))
    ko_min = (int(next_kickoff[3:5]))

    if ko_hour < (current_hour + 1):
        if ko_min > current_min:
            print(sleep_time * 3600)
            # time.sleep(sleep_time*3600) #sleep for 1 hour
    else:
        sleep_time = ko_hour - current_hour
        print(sleep_time * 3600)

    livescore_data = json.loads(requests.get(url).content)
    for match in livescore_data['data']:
        print(match['localTeam']['data']['name'])
    return (livescore_data)
