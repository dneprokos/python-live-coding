"""
- Implement a function that accepts a list of strings as ticket numbers.
- Each record range should be between 000001 and 100000.
- All numbers outside of this range should be ignored.
- It should return a list of only lucky numbers.
   - A lucky number is a number where the sum of the first three symbols is equal to the sum of the second three symbols.
"""

from typing import List


def get_lucky_ticket_numbers(tickets: List[str]) -> List[str]:
    # Init final list
    lucky_tickets: List[str] = []

    # Iterate throught tickets
    for ticket in tickets:
        # Verify length equals to 6 symbols and in range between 1 to 100000
        if not (ticket.isdigit() and (len(ticket) == 6 and 1 <= int(ticket) <= 100000)):
            continue
        # Convert to array of int
        int_list = [int(ch) for ch in ticket]

        # Compare two sums
        if sum(int_list[:3]) == sum(int_list[3:]):
            lucky_tickets.append(ticket)

    return lucky_tickets
