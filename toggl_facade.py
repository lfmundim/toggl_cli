from datetime import datetime

def get_timesheet_summary(entries):
    period_worked_hours = 0
    hours_per_day = dict()
    for entry in entries:
        start = entry['start']
        start_datetime = datetime.fromisoformat(start)
        start_date = start_datetime.date()
        hours = entry['duration']/3600
        if start_date in hours_per_day:
            hours_per_day[start_date] = hours_per_day[start_date] + hours
        else:
            hours_per_day[start_date] = hours
        period_worked_hours = period_worked_hours + hours

    for day, hours in hours_per_day.items():
        print(day, round(hours, 1))

    print(round(period_worked_hours, 1))
