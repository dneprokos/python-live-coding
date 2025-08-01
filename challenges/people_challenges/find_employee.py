from typing import List, Dict, Set

employees = [
    {"name": "Oleksandr Petrenko", "experience": 5, "position": "Developer"},
    {"name": "Maria Kovalenko", "experience": 2, "position": "Designer"},
    {"name": "Ivan Sydorenko", "experience": 7, "position": "Project Manager"},
    {"name": "Anna Melnyk", "experience": 1, "position": "Tester"},
    {"name": "Serhii Bondarenko", "experience": 4, "position": "Analyst"},
    {"name": "Kateryna Shevchenko", "experience": 6, "position": "Architect"},
    {"name": "Oleksandr Hrytsenko", "experience": 3, "position": "DevOps Engineer"},
]

# Create a function that takes array above and return unique (no duplicates) first names for employees work 3 and more years


def find_unique_first_name(employees: List[Dict[str, str]]) -> Set[str]:
    return set(emp.get("name").split(' ')[0] for emp in employees if emp.get("experience") >= 3)


def find_unqiue_first_names_without_duplicates(employees: List[Dict[str, str]]) -> List[str]:
    duplicates = dict()

    for emp in employees:
        if emp.get("experience") >= 3:
            first_name = emp.get("name").split(' ')[0]
            duplicates[first_name] = duplicates.get(first_name, 0) + 1

    return [key for key, value in duplicates.items() if value == 1]


print(find_unique_first_name(employees))
print(find_unqiue_first_names_without_duplicates(employees))
