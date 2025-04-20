# Challange: Create a function that adds to integers and returns the result


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
