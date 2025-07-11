
"""
Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse. For instance, given the number , its reverse is . Their difference is . The number  reversed is , and their difference is .

She decides to apply her game to decision making. She will look at a numbered range of days and will only go to a movie on a beautiful day.

Given a range of numbered days,  and a number , determine the number of days in the range that are beautiful. Beautiful numbers are defined as numbers where  is evenly divisible by . If a day's value is a beautiful number, it is a beautiful day. Return the number of beautiful days in the range.

Function Description

Complete the beautifulDays function in the editor below.

beautifulDays has the following parameter(s):

int i: the starting day number
int j: the ending day number
int k: the divisor
"""


def beautiful_days(first_b_day, last_b_day, devisible):
    """
    Counts the number of beautiful days between start_day and end_day (inclusive).

    A day is beautiful if the absolute difference between the day and its reverse
    is evenly divisible by the divisor.

    Parameters:
    - start_day (int): The starting day number.
    - end_day (int): The ending day number.
    - divisor (int): The number to check divisibility against.

    Returns:
    - int: Count of beautiful days.
    """
    # Form array of all days based on first and last day
    number_of_b_days = 0

    # Loop over the new array
    for day in range(first_b_day, last_b_day + 1):
        swap_number = int(str(day)[::-1])

        # if (current_number - swap_number) % devisible == 0:
        if (day - swap_number) % devisible == 0:
            number_of_b_days += 1

    return number_of_b_days
