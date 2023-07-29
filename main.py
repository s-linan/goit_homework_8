from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # current_day is data and time in this moment
    current_day = datetime.now()
    # dict to write birthdays for next week
    birthdays_next_week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
        'Saturday': [],
        'Sunday': []
    }
    # range for all next week
    range = current_day.date() + timedelta(weeks=1)

    for i in users:
        name = i['name']
        birthday = i['birthday']
        birthday = birthday.replace(year=datetime.today().year) # change all birth year to this year
        birthday_day = birthday.strftime('%A') # the name of the day of the week
        # if the birthday is in the next week from the current day we add it to dict
        if current_day.date() <= birthday.date() < range:
            # if birthday in Saturday or Sunday we move it to Monday
            if birthday_day in ['Saturday', 'Sunday']:
                birthday_day = 'Monday'
            birthdays_next_week[birthday_day].append(name)
    # output our birthday boys and girls
    for day, names in birthdays_next_week.items():
        if names:
            print(f"{day}: {', '.join(names)}")

# birthday list for example
users = [
    {"name": "Bob", "birthday": datetime(2000, 8, 4)},
    {"name": "Sam", "birthday": datetime(1995, 8, 1)},
    {"name": "Andrew", "birthday": datetime(1987, 7, 31)},
    {"name": "Lily", "birthday": datetime(1992, 7, 30)},
    {"name": "Samantha", "birthday": datetime(1998, 7, 29)},
]

get_birthdays_per_week(users)