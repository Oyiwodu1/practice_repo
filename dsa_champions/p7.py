def reverse_list(items):
    items.sort(reverse=True)
    return items
print(reverse_list([1, 5, 3, 4]))



def has_duplicate(numbers):
    seen_numbers = set()
    for number in numbers:
        if number in seen_numbers:
            return True
        seen_numbers.add(number)
    return False
print(has_duplicate([1, 2, 3, 2]))
print(has_duplicate([1, 2, 3, 4]))
