"""
A child is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds. The character must jump from cloud to cloud until it reaches the start again.

There is an array of clouds,  and an energy level . The character starts from  and uses  unit of energy to make a jump of size  to cloud . If it lands on a thundercloud, , its energy () decreases by  additional units. The game ends when the character lands back on cloud .

Given the values of , , and the configuration of the clouds as an array , determine the final value of  after the game ends.
"""

"""
#### Gameplay ####

---Game ends when:

- No Energy
- Player returned to position 0

---Variables
c - clouds
k - jump distance


--- Gameplay details
Standard jump uses 1 point of energy
If player lands on the cloud with value 1 (thunder), then we need to decrease additionaly 2 points of energy

"""


from typing import List
def jumping_on_clouds(c: List[int], k: int) -> int:
    """
    Simulate the "Jumping on the Clouds: Revisited" game.

    Rules (per your description):
    - The player starts at index 0 with 100 energy.
    - Each jump advances by k positions around the circular array of clouds.
    - Each jump costs 1 energy.
    - Landing on a thundercloud (value == 1) costs an additional 2 energy.
    - The game ends as soon as the player either:
        * returns to index 0 (after at least one jump), or
        * runs out of energy (energy <= 0).

    This implementation preserves your original logic (including the
    final clamp to 0 if energy went negative), but clarifies it with comments.

    Args:
        c: List[int] — cloud types; 0 = safe, 1 = thunder.
        k: int — fixed jump distance.

    Returns:
        int: Remaining energy at game end (never negative).
    """
    energy = 100          # Current player energy
    current_cloud = 0     # Cloud index where the player currently is

    while energy > 0:
        # Compute where the next landing would be if the array were linear.
        landing_point_index = current_cloud + k

        # Wrap the landing index if we would go past the end.
        # (This mimics modulo behavior without using % to keep your structure.)
        if landing_point_index > len(c) - 1:
            # Distance to the end from the current position
            left_jumps_to_end = (len(c) - 1) - current_cloud

            # "Overflow" beyond the end once we finish this jump
            temp_jump_dist = k - left_jumps_to_end

            # If the jump ends exactly at the last index, land there
            if temp_jump_dist == 0:
                landing_point_index = len(c) - 1
            else:
                # Otherwise wrap: -1 + overflow gives the correct 0-based index
                landing_point_index = -1 + temp_jump_dist

            current_cloud = landing_point_index
        else:
            # No wrap needed
            current_cloud = landing_point_index

        # Base jump cost (1) plus thunder penalty (2) if c[current_cloud] == 1
        energy = (energy - 1) - (2 if c[current_cloud] == 1 else 0)

        # Stop once we’ve returned to the starting cloud (index 0)
        if current_cloud == 0:
            break

    # Never return negative energy
    energy = 0 if energy < 0 else energy
    return energy


print(jumping_on_clouds([0, 0, 1, 0, 0, 1, 1, 0], 2))  # Expected: 92
print(jumping_on_clouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 3))  # Expected: 80
