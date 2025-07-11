import unittest

from challenges.hacker_rank.angry_professor import angry_professor


class TestAngryProfessor(unittest.TestCase):

    def test_class_cancelled(self):
        self.assertEqual(
            angry_professor(3, [-1, -3, 4, 2]),
            "YES"
        )

    def test_class_held(self):
        self.assertEqual(
            angry_professor(2, [0, -1, 2, 1]),
            "NO"
        )

    def test_all_on_time(self):
        self.assertEqual(
            angry_professor(1, [-1, 0, -3]),
            "NO"
        )

    def test_all_late(self):
        self.assertEqual(
            angry_professor(1, [1, 2, 3]),
            "YES"
        )

    def test_exact_threshold(self):
        self.assertEqual(
            angry_professor(2, [-1, 0, 1]),
            "NO"
        )

    def test_empty_list(self):
        self.assertEqual(
            angry_professor(1, []),
            "YES"
        )


if __name__ == '__main__':
    unittest.main()
