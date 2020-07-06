WORKOUT_SCHEDULE = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
REST, CHILL_OUT, TRAIN = 'Rest', 'Chill out!', 'Go train {}'
INVALID_DAY = 'Not a valid day'


def get_workout_motd(day):
    """First title case the passed in day argument
       (so monday or MONDAY both result in Monday).

       If day is not in WORKOUT_SCHEDULE, return INVALID_DAY

       If day is in WORKOUT_SCHEDULE retrieve the value (workout)
       and return the following:
       - weekday, return TRAIN with the workout value interpolated
       - weekend day (value 'Rest'), return CHILL_OUT

       Examples:
       - if day is Monday -> function returns 'Go train Chest+biceps'
       - if day is Thursday -> function returns 'Go train Legs'
       - if day is Saturday -> function returns 'Chill out!'
       - if day is nonsense -> function returns 'Not a valid day'

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'
    """
    if day.casefold() not in str(WORKOUT_SCHEDULE).casefold():
        print(INVALID_DAY)
        return INVALID_DAY
    else:
        if WORKOUT_SCHEDULE[day.capitalize()] == 'Rest':
            return CHILL_OUT
        else:
            print(TRAIN.format(WORKOUT_SCHEDULE[day.capitalize()]))
            return TRAIN.format(WORKOUT_SCHEDULE[day.capitalize()])


   # for key in WORKOUT_SCHEDULE:
   #     if key.casefold() == day.casefold():
   #         if key.casefold() == 'sunday':
   #             return REST
   #         if key.casefold() == 'saturday':
   #             return CHILL_OUT

   #pass

if __name__ == '__main__':
    get_workout_motd('monday')
