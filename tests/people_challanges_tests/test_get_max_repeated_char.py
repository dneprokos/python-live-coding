import pytest

from challenges.people_challanges.find_max_repeated_chars_in_string import get_max_repeated_char


def test_basic_sentence():
    assert get_max_repeated_char("hello world") == "l"


def test_case_insensitivity():
    assert get_max_repeated_char("AaAaBb") == "a"


def test_spaces_only():
    with pytest.raises(IndexError):  # No characters to analyze
        get_max_repeated_char("     ")


def test_empty_string():
    with pytest.raises(IndexError):  # No characters to analyze
        get_max_repeated_char("")


def test_all_unique():
    result = get_max_repeated_char("abcdefg")
    assert result in "abcdefg"  # Any one is valid since all appear once


def test_tie_characters():
    result = get_max_repeated_char("aabbcc")
    assert result in "abc"  # All tied with 2 occurrences


def test_special_characters():
    # All same freq, picks first by sort order
    assert get_max_repeated_char("$$##@@!!") == "$"


def test_numeric_characters():
    assert get_max_repeated_char("1122334455") in "12345"
