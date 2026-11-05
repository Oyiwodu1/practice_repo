def safe_divide(a, b):
    if b == 0:
        return "cannot be divided by zero"
    return round(a / b, 2)
print(safe_divide(10, 2))
print(safe_divide(10, 0))


def get_item(items, index):
    if index < 0 or index >= len(items):
        return "Index out of range"
    return items[index]

def grade_label(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"
print(grade_label(101))
print(grade_label(95))
print(grade_label(10))

def count_up(n):
    count = []
    if n < 1:
        return count
    for numbers in range(1, (n + 1)):
        count.append(numbers)
    return count
print(count_up(5))
print(count_up(1))

def sum_multiples(limit, divisor):
    if divisor == 0:
        return "Invalid divisor"
    total = 0
    for numbers in range(1,(limit + 1)):
        if numbers % divisor == 0:
            total += numbers
    return total
print(sum_multiples(10, 3))
print(sum_multiples(20, 5))

def count_until_stop(items):
    collected = []
    for item in items:
        seen = item.strip().lower()
        if seen == "stop":
            break
        collected.append(item)
    return collected
print(count_until_stop(["red","blue","stop","green"]))
print(count_until_stop(["stop","red"]))

def skip_evens(start, end):
    odd_numbers = []
    if start > end:
        return odd_numbers
    for numbers in range(start, end + 1):
        if numbers % 2 == 0:
            continue
        odd_numbers.append(numbers)
    return odd_numbers
print(skip_evens(1, 10))

def triangle_pattern(n):
    if n < 1:
        return ""
    pattern = ""
    for numbers in range(1, n + 1):
        pattern += "*" * numbers
        if numbers < n:
            pattern += "\n"
    return pattern

def prime_list(n):
    prime = []
    for numbers in range(2, (n + 1)):
        is_prime = True
        for divisor in range(2, numbers -1):
            if numbers % divisor == 0:
                is_prime = False
                break
        if is_prime == True:
            prime.append(numbers)
    return prime
print(prime_list(10))

def reciept_formatter(name, quantity, price):
    subtotal = quantity * price
    tax = subtotal * 0.075
    total = subtotal + tax
    
    subtotal = round(subtotal, 2)
    tax = round(tax, 2)
    total = round(total, 2)

    report = (
        f"Customer: {name}\n"
        f"Subtotal: {subtotal:.1f}\n"
        f"Tax: {tax}\n"
        f"Total: {total}"
    )
    return report
print(reciept_formatter("Ada", 2, 100))