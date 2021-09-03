from datetime import datetime
from utils import get_token, get_current_month_first_day, get_current_month_last_day
from datetime import datetime
from models.timesheet_summary import TimesheetSummary
import toggl_api

def get_timesheet_summary(args):
    api_key = get_token(args)

    base64_key = toggl_api.create_authorization(api_key)

    start_date = args.start if args.start is not None else str(get_current_month_first_day())
    end_date = args.end if args.end is not None else str(get_current_month_last_day())
    print(start_date, end_date)

    entries = toggl_api.get_time_entries_from_period(start_date, end_date, base64_key)

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
