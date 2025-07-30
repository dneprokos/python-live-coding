import pytest

from challenges.hacker_rank.halloween_sale import how_many_games


@pytest.mark.parametrize("p, d, m, s, expected", [
    (20, 3, 6, 80, 6),
    (20, 3, 6, 85, 7),
    (20, 3, 6, 0, 0),
    (20, 3, 6, 20, 1),
    (20, 3, 6, 19, 0),
    (5, 2, 1, 10, 4),
])
def test_how_many_games(p, d, m, s, expected):
    assert how_many_games(p, d, m, s) == expected
