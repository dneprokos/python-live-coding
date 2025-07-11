import unittest

from challenges.hacker_rank.the_hurdle_race import hurdle_race


class TestHurdleRace(unittest.TestCase):

    def test_no_dose_needed(self):
        # Max height = 1, k = 5 → no dose needed
        self.assertEqual(hurdle_race(5, [1, 2, 1]), 0)

    def test_exact_jump_needed(self):
        # Max height = 7, k = 7 → jump just enough
        self.assertEqual(hurdle_race(7, [2, 4, 7, 1]), 0)

    def test_dose_needed(self):
        # Max height = 9, k = 4 → need 5 doses
        self.assertEqual(hurdle_race(4, [1, 6, 9, 3]), 5)

    def test_all_equal_to_k(self):
        # All hurdles = 3, k = 3 → no dose
        self.assertEqual(hurdle_race(3, [3, 3, 3]), 0)

    def test_single_hurdle(self):
        # Only one hurdle, higher than k
        self.assertEqual(hurdle_race(1, [5]), 4)

    def test_empty_list(self):
        # No hurdles, no dose needed
        with self.assertRaises(ValueError):
            hurdle_race(5, [])  # max() on empty list raises ValueError


if __name__ == '__main__':
    unittest.main()
