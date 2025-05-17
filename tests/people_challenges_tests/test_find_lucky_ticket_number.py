from challenges.people_challenges.find_lucky_ticket_number import get_lucky_ticket_numbers


def test_valid_lucky_ticket():
    assert get_lucky_ticket_numbers(["001001"]) == ["001001"]


def test_valid_unlucky_ticket():
    assert get_lucky_ticket_numbers(["123456"]) == []


def test_invalid_ticket_too_short():
    assert get_lucky_ticket_numbers(["12345"]) == []


def test_invalid_ticket_non_numeric():
    assert get_lucky_ticket_numbers(["12a456"]) == []


def test_ticket_out_of_range_zero():
    assert get_lucky_ticket_numbers(["000000"]) == []


def test_ticket_out_of_range_high():
    assert get_lucky_ticket_numbers(["100001"]) == []


def test_mixed_valid_and_invalid():
    tickets = ["001001", "123456", "abc123", "000000", "100000"]
    assert get_lucky_ticket_numbers(tickets) == ["001001"]


def test_less_than_min_symbols():
    tickets = ["12345"]
    assert get_lucky_ticket_numbers(tickets) == []
