def count_occurrences(numbers, target):
    count = 0
    for number in numbers:
        if number == target:
            count +=1
    return count
print(count_occurrences([2, 5, 2, 8, 2], 2))




def find_number(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1
print(find_number([10, 25, 30, 45], 30))
print(find_number([5, 8, 5, 9], 5))
print(find_number([10, 20, 30], 99))