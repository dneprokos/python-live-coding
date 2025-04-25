# Challange: Create a function that adds to integers and returns the result

"""
Complete the function  to compute the sum of two integers.

Example


Return .

Function Description

Complete the  function with the following parameters:

: the first value
: the second value
Returns
- : the sum of  and 
"""


def add(a: int, b: int) -> int:
    """
    Adds two integers together.

    Parameters:
        a (int): The first number to add.
        b (int): The second number to add.

    Returns:
        int: The sum of the two integers.

    Raises:
        TypeError: If either input is not an integer.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")
    return a + b
