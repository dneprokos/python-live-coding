import pytest

from challenges.hacker_rank.jumping_on_the_clouds import jumping_on_clouds


@pytest.mark.parametrize(
    "c,k,expected",
    [
        # Provided examples
        ([0, 0, 1, 0, 0, 1, 1, 0], 2, 92),
        ([1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 3, 80),
    ],
)
def test_given_examples(c, k, expected):
    assert jumping_on_clouds(c, k) == expected


def test_all_safe_clouds_even_wrap():
    # N=8, k=2 → jumps: 0→2→4→6→0 (4 jumps; each costs 1)
    c = [0] * 8
    assert jumping_on_clouds(c, 2) == 100 - 4 * 1  # 96


def test_all_thunderclouds_small_circle():
    # N=6, k=2 → 0→2→4→0 (3 jumps; each costs 3)
    c = [1] * 6
    assert jumping_on_clouds(c, 2) == 100 - 3 * 3  # 91


def test_k_equals_n_safe_start():
    # k == N means we return to 0 in exactly one jump.
    c = [0, 1, 0, 1]
    # One jump, safe landing: -1
    assert jumping_on_clouds(c, len(c)) == 99


def test_k_equals_n_thunder_start():
    # Starting cloud is thunder, but the penalty applies only when we LAND on it again.
    c = [1, 0, 0, 0]
    # One jump, land back on index 0 which is thunder: -1 -2
    assert jumping_on_clouds(c, len(c)) == 97


def test_gcd_case_multiple_visits_before_return():
    # N=10, k=4 (gcd=2). Path length to return to 0 is N/gcd = 5 jumps.
    # Choose a pattern to mix thunder and safe.
    c = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]  # indexes 1,3,5,7,9 are thunder
    # Path starting at 0 with k=4: 0->4(0)->8(0)->2(0)->6(0)->0(0)
    # All safe on visited landings. 5 jumps * 1 energy each = -5
    assert jumping_on_clouds(c, 4) == 95


def test_energy_runs_out_before_return():
    # Many thunder hits with k=1; make N large to exhaust energy before we get back.
    N = 40
    c = [1] * N  # every landing is thunder (cost 3 per jump)
    # After 33 jumps: energy = 100 - 33*3 = 1
    # After 34th jump: energy = -2 (loop stops next check; function clamps to 0)
    result = jumping_on_clouds(c, 1)
    assert result == 0
