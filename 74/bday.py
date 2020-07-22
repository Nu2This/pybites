import calendar
from datetime import date


def weekday_of_birth_date(date):
    """Takes a date object and returns the corresponding weekday string"""
    days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
            4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    print(calendar.weekday(date.year, date.month, date.day))
    print(days[calendar.weekday(date.year, date.month, date.day)])
    return days[calendar.weekday(date.year, date.month, date.day)]

if __name__ == '__main__':
    weekday_of_birth_date(date(1974,11,11))
