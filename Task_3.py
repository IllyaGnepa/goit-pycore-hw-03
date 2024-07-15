import re

def normalize_phone(phone_number):
    try:
        # Removal of all symbols, in order to leave only numbers
        remove_symbols = re.sub(r"[\D.]", "", phone_number)

        # Searching for the first zero in number and changing everything before it to +380
        modify  = re.sub(r"^.*?0", "+380", remove_symbols, count=1)    
        return modify
    except TypeError:
        print(f"Please provide numbers")