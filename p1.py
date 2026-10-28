def find_largest(numbers):
    if numbers == []:
        return None

    highest_number = numbers[0]
    for number in numbers:
        if number > highest_number:
            highest_number = number
    return highest_number
print(find_largest([3, 41, 56, 21, 76, 9]))




def find_smallest(numbers):
    if numbers == []:
        return None

    smallest_number = numbers[0]
    for number in numbers:
        if number < smallest_number:
            smallest_number = number
    return smallest_number
print(find_smallest([8, 3, 12, 1, 7]))