def list_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(list_sum([2, 4, 6, 8]))




def count_even(numbers):
    even_numbers = 0
    for number in numbers:
        if number % 2 == 0:
            even_numbers +=1
    return even_numbers
print(count_even([1, 2, 3, 4, 5, 6]))