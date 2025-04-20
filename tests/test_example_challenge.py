from challenges.example_challenge import add
import pytest


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -2) == -3


def test_add_zero():
    assert add(0, 5) == 5


def test_add_with_string_input():
    with pytest.raises(TypeError):
        add("2", 3)


def test_add_with_float_input():
    with pytest.raises(TypeError):
        add(2.5, 3)


def test_add_with_list_input():
    with pytest.raises(TypeError):
        add([1], 3)


def test_add_with_none_input():
    with pytest.raises(TypeError):
        add(None, 3)
