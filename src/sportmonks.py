# Retrieve fixtures for today
def get_fixtures():
    # Check if fixture file exists for today, if so do nothing
    try:
        filename = '/home/mark/SPL_Updates/data/fixtures/' + check_date + '.json'
        f = open(filename, 'r')
        fixture_dict = json.loads(f.read())
        f.close()
        print(fixture_dict)
        add_log('retrieved fixtures from ' + filename)  # logging

    # If fixtures files doesn't exist then proceed with checking the api endpoint for new fixtures
    except:
        add_log('checking for new fixtures')  # logging
        url = fixtures_url + todays_date + soccer_api + fixture_includes
        fixtures = json.loads(requests.get(url).content)
        add_log('finished checking for new fixtures')  # logging
        fixture_dict = {}
        fixture_list = "Today's Fixtures:\n\n"

        # Check fixture is for the SPL (League code 501)
        for f in fixtures['data']:
            if f['league_id'] == league_code:
                fixture = f['localTeam']['data']['name']
                fixture += ' vs '
                fixture += f['visitorTeam']['data']['name']
                fixture_list += fixture
                fixture_list += '\n'
                fixture_dict[fixture] = {'id': f['id'], 'start_time': f['time']['starting_at']['time']}
                print(fixture)
                print(fixture_dict)
            else:
                pass

        # If length of fixture_list is > 19 then new fixtures must be happening today so Tweet the day's fixtures
        if len(fixture_list) != 19:
            add_log("tweeting today's fixtures")  # logging
            post_tweet(fixture_list)
            filename = '/home/mark/SPL_Updates/data/fixtures/' + check_date + '.json'
            file = open(filename, 'w')
            add_log("adding today's fixtures to " + filename)  # logging
            file.write(json.dumps(fixture_dict, indent=4))
            file.close
        # Otherwise simply tweet there are no new fixtures today + the date
        else:
            add_log("tweeting there are no fixtures today")  # logging
            post_tweet('There are no SPL games today (' + check_date + ')')
    return (fixture_dict)


# Livescore Updates
def get_updates():
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
