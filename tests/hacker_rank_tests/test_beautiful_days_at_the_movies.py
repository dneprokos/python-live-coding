import unittest

from challenges.hacker_rank.beautiful_days_at_the_movies import beautiful_days


class TestBeautifulDays(unittest.TestCase):

    def test_basic_case(self):
        # Days: 20, 21, 22, 23 → Reversed: 02, 12, 22, 32
        # (20–2)=18 % 6==0 → ✅
        # (21–12)=9 % 6==3 → ❌
        # (22–22)=0 % 6==0 → ✅
        # (23–32)=9 % 6==3 → ❌
        self.assertEqual(beautiful_days(20, 23, 6), 2)

    def test_all_beautiful(self):
        # 1 to 10, divisor=1 → all differences are divisible by 1
        self.assertEqual(beautiful_days(1, 10, 1), 10)

    def test_some_beautiful(self):
        # Only 11 is beautiful in this range
        self.assertEqual(beautiful_days(10, 12, 2), 1)

    def test_single_day_beautiful(self):
        # 7 - 7 = 0 % 1 = 0 → beautiful
        self.assertEqual(beautiful_days(7, 7, 1), 1)

    def test_large_range(self):
        # Verified: 10 beautiful days between 100 and 200 when divisor is 13
        self.assertEqual(beautiful_days(100, 200, 13), 10)

    def test_no_beautiful_days(self):
        # Only 11 is beautiful since difference is 0
        self.assertEqual(beautiful_days(10, 20, 100), 1)


if __name__ == '__main__':
    unittest.main()
