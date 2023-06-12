from datetime import timedelta, datetime
import calendar

def get_birthdays_per_week(users):
    today = datetime.now()
    one_week = timedelta(days=7)
    birthdays = {}
    for user in users:
        name = user['name']
        birthday = user['birthday']
        b = birthday.replace(year=today.year)           # to know the weekday this year
        if birthday.strftime('%B %d') == today.strftime('%B %d'): 
            add_to_birthdays(birthdays, 'Today', name)
        elif today.strftime('%B %d') < birthday.strftime('%B %d') < (today + one_week).strftime('%B %d'):   # birthday < today + 7                        
            weekday = calendar.day_name[b.weekday()]    # weekday - str type (Monday, Tuesday etc.)
            if weekday == ('Saturday' or 'Sunday'):
                add_to_birthdays(birthdays, 'Will be on weekends, next Monday', name)
            else:
                add_to_birthdays(birthdays, weekday, name)
        elif today.weekday() == 0 and today - b < timedelta(days = 3):
            add_to_birthdays(birthdays, 'Was on weekends, Today', name)

    if birthdays:
        for key, value in birthdays.items():
            print(f"{key}: {', '.join(value)}")         # output according technical specifications 
    else:
        print("Value not found")
        
def add_to_birthdays(dictonary, day , name):    
    if day not in dictonary:            # check if key exists             
        dictonary[day] = [name]         # create new key with list value (with name of the person)     
    else:                               # key exists                      
        dictonary[day].append(name)     # append new value to existing list
