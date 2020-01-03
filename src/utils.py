import datetime
import json

with open('./config.json', 'r') as config_file:
    config = json.load(config_file)

today = datetime.datetime.now() #Raw date


def add_log(text):
    log = open(config['log_file'], 'a')
    log.write('*** ' + str(today) + ' *** ' + text + '\n')
    log.close()
