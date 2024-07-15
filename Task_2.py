import random

def get_numbers_ticket(min: int, max: int, quantity):

    try:
        # Check if provided numbers are within required range
        if min < 1 or max > 1000:
            print(f"Numbers can be picked only between 1 and 1000")
        else: 
            # Generating range to pick lottery numbers
            numbers = range(min, max)

            # Pick and sort lottery numbers
            lottery_numbers = sorted(random.sample(numbers, k=quantity))
            print("Ваші лотерейні числа:", lottery_numbers)
    except TypeError:
        print(f"Please provide numbers")