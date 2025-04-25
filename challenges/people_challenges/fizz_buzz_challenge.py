# Create a function that accepts an integer
# Якщо номер кратний тільки 3, то ми повинні повертати "fizz"
# Якщо номер кратний тільки 5, то ми повинні повертати "buzz"
# Якщо номер кратний 3 та 5, то ми повинні повертати "fizzbuzz"
# Якщо не підходить, то повертаємо номер

def fizz_buzz_solving(input) -> str:
    # перевіряємо, що тип інтеджер і не пустий
    if not isinstance(input, int):
        return input
    # переврямо чи номер кратний 3 та 5
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizzbuzz"
    # переврямо чи номер кратний 3
    if (input % 3 == 0):
        return "fizz"
    # переврямо чи номер кратний 5
    if (input % 5 == 0):
        return "buzz"
    # якщо ні, то виводимо інпут
    return str(input)
