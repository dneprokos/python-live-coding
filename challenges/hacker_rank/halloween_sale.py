"""
You wish to buy video games from the famous online video game store Mist.
Usually, all games are sold at the same price, p dollars. However, they are planning to have the seasonal 
Halloween Sale next month in which you can buy games at a cheaper price. 
Specifically, the first game will cost p dollars, and every subsequent game will cost d dollars less than the previous one. 
This continues until the cost becomes less than or equal to  dollars, after which every game will cost m dollars. 
How many games can you buy during the Halloween Sale?
"""


def how_many_games(p: int, d: int, m: int, s: int) -> int:
    """
        Complete the 'howManyGames' function below.

        The function is expected to return an INTEGER.
        The function accepts following parameters:
         1. INTEGER p - Sarting price
         2. INTEGER d - discount for the next game
         3. INTEGER m - minimal price
         4. INTEGER s - budget
    """
    games_to_buy = 0
    current_game_cost = p

    while (s > 0):
        if (s >= current_game_cost):
            games_to_buy += 1
            s -= current_game_cost

            if (current_game_cost - d <= m):
                current_game_cost = m
            else:
                current_game_cost -= d
        else:
            break

    return games_to_buy


print(how_many_games(20, 3, 6, 80))  # Expected 6
print(how_many_games(20, 3, 6, 85))  # Expected 7
print(int())
