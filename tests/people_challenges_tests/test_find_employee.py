import pytest

from challenges.people_challenges.find_employee import find_unique_first_name, find_unqiue_first_names_without_duplicates

employees = [
    {"name": "Oleksandr Petrenko", "experience": 5, "position": "Developer"},
    {"name": "Maria Kovalenko", "experience": 2, "position": "Designer"},
    {"name": "Ivan Sydorenko", "experience": 7, "position": "Project Manager"},
    {"name": "Anna Melnyk", "experience": 1, "position": "Tester"},
    {"name": "Serhii Bondarenko", "experience": 4, "position": "Analyst"},
    {"name": "Kateryna Shevchenko", "experience": 6, "position": "Architect"},
    {"name": "Oleksandr Hrytsenko", "experience": 3, "position": "DevOps Engineer"},
]


def test_find_unique_first_name():
    result = find_unique_first_name(employees)
    expected = {"Oleksandr", "Ivan", "Serhii", "Kateryna"}
    assert set(result) == expected


def test_find_unqiue_first_names_without_duplicates():
    result = find_unqiue_first_names_without_duplicates(employees)
    expected = ["Ivan", "Serhii", "Kateryna"]  # Oleksandr appears twice
    assert set(result) == set(expected)


def test_empty_employee_list():
    assert find_unique_first_name([]) == set()
    assert find_unqiue_first_names_without_duplicates([]) == []


def test_all_employees_under_3_years():
    low_exp = [
        {"name": "Junior Dev", "experience": 2, "position": "Developer"},
        {"name": "Intern", "experience": 1, "position": "Support"},
    ]
    assert find_unique_first_name(low_exp) == set()
    assert find_unqiue_first_names_without_duplicates(low_exp) == []


def test_duplicate_names_with_experience():
    dup_employees = employees + \
        [{"name": "Ivan Petrov", "experience": 5, "position": "Analyst"}]
    result = find_unqiue_first_names_without_duplicates(dup_employees)
    assert "Ivan" not in result
