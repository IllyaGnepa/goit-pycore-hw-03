from datetime import datetime

def get_days_from_today(date):
    # Check if provided date is in correct format and type
    try: 
        datetime_object = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Please use correct date format - YYYY-MM-DD")
        return
    except (TypeError):
        print("Please provide date as a string")
        return


    # Dates difference calculation
    difference = datetime_object - datetime.today()

    print(int(difference.days))