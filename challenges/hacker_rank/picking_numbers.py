"""
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to .

Example


There are two subarrays meeting the criterion:  and . The maximum length subarray has  elements.
"""

from typing import List


def pickingNumbers(a: List[int]):
    # create temp array
    numbersArr = a
    tempNums = []
    firstNumber = numbersArr[0]
    tempNums.append(firstNumber)
    for index, el in enumerate(numbersArr):
        if index == 0:
            continue
        if (abs(firstNumber - el) == 1 or firstNumber - el == 0):
            if (len(tempNums) < 5):
                tempNums.append(el)
    indexToRemove: list[int] = []
    for index in range(len(tempNums) - 1):
        if not (abs(tempNums[index] - tempNums[index + 1]) == 1 or tempNums[index] - tempNums[index + 1] == 0):
            indexToRemove.append(index)
    if (len(indexToRemove) >= 1):
        tempNums.pop(indexToRemove[0])
    print(tempNums)
    return len(tempNums)

    # abc_numbers: List[int] = [[]]
    # current_max_length = 0

    # for index, number in enumerate(numbers):
    #     inner_array = [number]

    #     current_number = numbers[index]

    #     for inner_index, inner_number in enumerate(numbers):
    #         if not index == inner_index and (abs(current_number - inner_number) <= 1 and len(inner_array) < 5):
    #             inner_array.append(inner_number)

    #     print(inner_array)

    #     abc_numbers.append(inner_array)

    # for number in abc_numbers:
    #     if len(number) > current_max_length:
    #         current_max_length = len(number)

    # return current_max_length


print(pickingNumbers([1, 2, 2, 3, 1, 2]))
print(pickingNumbers([4, 6, 5, 3, 3, 1]))
