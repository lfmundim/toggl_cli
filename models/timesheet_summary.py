from datetime import datetime
from utils import to_table

class TimesheetSummary:
    def __init__(self, start, end, period_hours, timesheet):
        self.start = start
        self.end = end
        self.period_hours = period_hours
        self.timesheet = timesheet

    start = datetime.now
    end = datetime.now
    period_hours = 0
    timesheet = dict()

    def __str__(self):
        copy = dict(self.timesheet)
        copy['Total     '] = self.period_hours

        return to_table(copy)