from datetime import datetime, timedelta, date

def get_birthdays_per_week(users):
    # current_day is data and time in this moment
    current_day = date.today()
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # dict to write birthdays for next week
    birthdays_next_week = {i: [] for i in range(7)}
    # end_date for all next week
    end_date = current_day + timedelta(weeks=1)

    for user in users:
        name = user['name']
        birthday = user['birthday'].replace(year=datetime.today().year) # change all birth year to this year
        birthday_day = birthday.weekday() # numerical order of the day of the week
        # if today is Monday, we need to go back 2 days to include birthdays that were on the weekend
        if current_day.weekday() == 0:
            current_day = current_day - timedelta(days=2)
        # if the birthday is in the next week from the current day we add it to dict
        if current_day <= birthday.date() < end_date:
            # if birthday in Saturday or Sunday we move it to Monday
            if birthday_day in [5, 6]:
                birthday_day = 0
            birthdays_next_week[birthday_day].append(name)
    # output our birthday boys and girls
    for day, names in birthdays_next_week.items():
        if names:
            print(f"{days[day]}: {', '.join(names)}")

# birthday list for example
users = [
    {"name": "Bob", "birthday": datetime(2000, 8, 4)},
    {"name": "Sam", "birthday": datetime(1995, 8, 1)},
    {"name": "Andrew", "birthday": datetime(1987, 7, 31)},
    {"name": "Lily", "birthday": datetime(1992, 7, 30)},
    {"name": "Samantha", "birthday": datetime(1998, 7, 29)},
]

get_birthdays_per_week(users)