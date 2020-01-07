import datetime
import json

with open('./config.json', 'r') as config_file:
    config = json.load(config_file)


def add_log(text):
    today = datetime.datetime.now()  # Raw date
    log = open(config['log_file'], 'a')
    log.write('*** ' + str(today) + ' *** ' + text + '\n')
    log.close()


def time_to_sleep(wake_time):
    """
    :param: wake_time format HH:MM
    :return: returns total seconds until wake_time
    """

    current_time = datetime.datetime.today()
    current_hour = (int(current_time.hour))
    wake_hour = (int(wake_time[0:2]))
    current_min = (int(current_time.minute))
    wake_min = (int(wake_time[3:5]))
    sleep_time = 0

    # Handle where wake_time is between 23-24 hours away
    if wake_hour == current_hour and wake_min < current_min:
        sleep_time = 23 * 60

    elif wake_hour == current_hour and wake_min > current_min:
        sleep_time = wake_min - (current_min + 1)

    # Calc Hours
    if wake_hour < current_hour and wake_min > current_min:
        sleep_time += (24 - current_hour) * 60
        sleep_time += wake_hour * 60

    elif wake_hour < current_hour:
        sleep_time += (24 - current_hour) * 60
        sleep_time += (wake_hour - 1) * 60

    elif wake_hour >= current_hour + 1 and wake_min > current_min:
        sleep_time += (wake_hour - current_hour) * 60

    elif wake_hour > current_hour + 1:
        sleep_time += (wake_hour - (current_hour + 1)) * 60

    elif wake_hour > current_hour and wake_min > current_min:
        sleep_time += 60

    else:
        pass

    # Calc minutes
    if wake_min < current_min:
        sleep_time += 60 - (current_min + 1) + wake_min

    elif wake_min > current_min:
        sleep_time += wake_min - (current_min + 1)

    # Testing outputs
    # sleep_hours = sleep_time // 60
    # sleep_mins = sleep_time - (sleep_hours * 60)
    # if sleep_hours < 10:
    #     sleep_hours = f'0{sleep_hours}'
    # if sleep_mins < 10:
    #     sleep_mins = f'0{sleep_mins}'
    # if current_hour < 10:
    #     current_hour = f'0{current_hour}'
    # if current_min < 10:
    #     current_min = f'0{current_min}'
    # if wake_hour < 10:
    #     wake_hour = f'0{wake_hour}'
    # if wake_min < 10:
    #     wake_min = f'0{wake_min}'
    #
    # print(f'Current time - {current_hour}:{current_min}')
    # print(f'Wake time - {wake_hour}:{wake_min}')
    # print(f'Time to sleep - {sleep_hours}:{sleep_mins}')

    return sleep_time * 60


def date_today():  # YYYY-MM-DD Format
    today = datetime.datetime.now()  # Raw date
    date_today = today.strftime('%Y') + '-' + today.strftime('%m') + '-' + today.strftime('%d')
    return date_today


def check_date():  # DD-MMM-YYYY Format
    today = datetime.datetime.now()  # Raw date
    check_date = today.strftime('%d') + '-' + today.strftime('%B') + '-' + today.strftime('%Y')
    return check_date


def prettify_json(raw_json):
    with open(raw_json) as json_file:
        parsed = json.load(json_file)
        pretty_json = (json.dumps(parsed, indent=4, sort_keys=True))
    return pretty_json
