from utils import home, dict_to_csv
from configparser import ConfigParser
import toggl_facade
import os

def configure(args):
    api_key = args.key
    if api_key:
        config_object = ConfigParser()
        config_object['USERINFO'] = {
            'token': api_key
        }

        try:
            os.mkdir(home+'/.toggl')
        except FileExistsError:
            print('File already exists. Replaced Token.')

        with open(home+'/.toggl/config.ini', 'w+') as conf:
            config_object.write(conf)
    else:
        print('No argument --key passed')

def timesheet(args):
    summary = toggl_facade.get_timesheet_summary(args)
    if args.json:
        print(summary.__dict__)
    elif args.csv:
        header = ['day', 'hours']
        print(dict_to_csv(dict(summary.timesheet), header))
    else:
        print(str(summary))