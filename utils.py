import os
from configparser import ConfigParser
from datetime import datetime, timedelta

home = os.path.expanduser('~')

def get_token(args):
    if args.file:
        config_object = ConfigParser()
        config_object.read(home+'/.toggl/config.ini')
        return config_object['USERINFO']['token']
    else:
        return args.key

def to_table(obj):
    if type(obj) is not dict:
        raise TypeError()

    return ''.join(['{} {}\n'.format(key, value) for key, value in obj.items()])

def dict_to_csv(obj, header=None):
    if type(obj) is not dict:
        print(type(obj))
        raise TypeError()

    csv = ''.join(['{},{}\n'.format(key, value) for key, value in obj.items()])

    return csv if header is None else '{},{}\n'.format(header[0], header[1]) + csv

def get_current_month_first_day():
    return datetime \
        .today() \
        .replace(day=1, hour=0, minute=0, second=0, microsecond=0) \
        .date()

def get_current_month_last_day():
    date = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    if date.month == 12:
        return date.replace(day=31).date()
    return (date.replace(month=date.month+1, day=1) - timedelta(days=1)).date()
