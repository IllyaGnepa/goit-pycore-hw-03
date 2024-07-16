#import datetime 
from datetime import datetime
from datetime import timedelta

def get_upcoming_birthdays(users):
    # Prepare a list for results
    upcoming_birthdays = []
    # Handling error when there is no name or birthday. Wrong time format error is informative enough, there is no need to handle that type of errors.
    try:
        # Checking every user in a provided list
        for user in users:
            
            # Reading birthday date
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d")
            
            # Changing year to current, to get upcoming birthday
            birthday_this_year = birthday.replace(year=datetime.today().year)
            
            # Checking if user celebrated birthday already this year.
            # If yes - adding one more year
            if birthday_this_year < datetime.today():
                birthday_this_year = birthday.replace(year=datetime.today().year+1)  
            
            # Checking if upcoming birthday is within next 7 days
            if birthday_this_year >= datetime.today() and birthday_this_year <= (datetime.today() + timedelta(days=6)):
                
                # Checking if birthday is on a weekend
                # If yes - move congratulation day to Monday
                if birthday_this_year.isoweekday() == 6 or birthday_this_year.isoweekday() == 7:
                    upcoming_birthday = birthday_this_year + timedelta(days=8-birthday_this_year.isoweekday())
                else:
                    upcoming_birthday = birthday_this_year
            
                # Add user name and congratulation date to the result list
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": upcoming_birthday.strftime("%Y.%m.%d")})
        
        # Print a message if there will be no birthdays this week
        if upcoming_birthdays == []:
            print(f"No birthdays this week")
        else: 
            return upcoming_birthdays
        
    except KeyError:
        print(f"Please provide both: name and birthday")