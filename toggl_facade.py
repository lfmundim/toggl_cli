from datetime import datetime
from utils import home
from configparser import ConfigParser
from models.timesheet_summary import TimesheetSummary
import toggl_api

def get_timesheet_summary(args):
    if args.file:
        config_object = ConfigParser()
        config_object.read(home+'/.toggl/config.ini')
        api_key = config_object['USERINFO']['token']
    else:
        api_key = args.key

    base64_key = toggl_api.create_authorization(api_key)
    entries = toggl_api.get_time_entries_from_period(args.start, args.end, base64_key)

    period_worked_hours = 0
    hours_per_day = dict()

    for entry in entries:
        start = entry['start']
        start_datetime = datetime.fromisoformat(start)
        start_date = start_datetime.date()
        hours = entry['duration']/3600
        if start_date in hours_per_day:
            hours_per_day[start_date] = round(hours_per_day[start_date] + hours, 1)
        else:
            hours_per_day[start_date] = round(hours, 1)
        period_worked_hours = period_worked_hours + hours

    response = TimesheetSummary(args.start, args.end, round(period_worked_hours, 1), hours_per_day.items())

    return response
