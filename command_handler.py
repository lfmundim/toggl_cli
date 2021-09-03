import os
import toggl_api
import toggl_facade
from configparser import ConfigParser

home = os.path.expanduser('~')

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
    if args.file:
        config_object = ConfigParser()
        config_object.read(home+'/.toggl/config.ini')
        api_key = config_object['USERINFO']['token']
    else:
        api_key = args.key

    base64_key = toggl_api.create_authorization(api_key)
    entries = toggl_api.get_time_entries_from_period(args.start, args.end, base64_key)

    toggl_facade.get_timesheet_summary(entries)