"""
A jail has a number of prisoners and a number of treats to pass out to them. 
Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs. 
A chair number will be drawn from a hat. Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially 
around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. 
Determine the chair number occupied by the prisoner who will receive that candy.
"""


def save_the_prisoner(n: int, m: int, s: int) -> int:
    """
    The function is expected to return an INTEGER.
    The function accepts following parameters:
     1. INTEGER n - number of priseners
     2. INTEGER m - quanity of candies 
     3. INTEGER s - starting chair number
    """

    number_of_candies = m
    chairs = [x for x in range(n)]
    current_chair_index = s - 1

    while (number_of_candies > 0):
        if (number_of_candies == 1):
            return current_chair_index + 1

        # Decrease candies number
        number_of_candies -= 1

        # Find next chair index
        if (len(chairs) < current_chair_index + 1):
            current_chair_index = 0
        else:
            current_chair_index = current_chair_index + 1


print(save_the_prisoner(5, 2, 1))  # Expected 2
print(save_the_prisoner(7, 19, 2))  # Expected 6
print(save_the_prisoner(3, 7, 3))  # Expected 3
