import pytest
from challenges.people_challenges.fizz_buzz_challenge import fizz_buzz_solving


def test_should_return_fizz():
    assert fizz_buzz_solving(3) == "fizz"


def test_should_return_buzz():
    assert fizz_buzz_solving(5) == "buzz"


def test_should_return_fizzbuzz():
    assert fizz_buzz_solving(15) == "fizzbuzz"


def test_should_return_two():
    assert fizz_buzz_solving(2) == "2"


def test_should_return_a():
    assert fizz_buzz_solving("a") == "a"
