"""A video player plays a game in which the character competes in a hurdle race. 
Hurdles are of varying heights, and the characters have a maximum height they can jump. 
There is a magic potion they can take that will increase their maximum jump height by  unit for each dose. 
How many doses of the potion must the character take to be able to jump all of the hurdles. 
If the character can already clear all of the hurdles, return .

Example
The character can jump  unit high initially and must take  doses of potion to be able to jump all of the hurdles. """


def hurdle_race(k, height):
    # Find maximum height
    max_h = max(height)

    # Decrease maximum height
    result = max_h - k

    # If value < 0 return 0
    if result < 0:
        return 0
    return result

    # Python style solution
    # required_dose = max(heights) - k
    # return max(0, required_dose)
