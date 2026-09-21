shopping = ["bread", "milk"]
shopping.append("rice")
shopping[1] = "juice"
shopping.remove("bread")
print(shopping)

fruits = ["apple", "mango", "banana", "orange"]
for fruit in fruits:
    print(fruit)

numbers = [5, 12, 8, 20, 3]
for number in numbers:
    if number > 10:
        print(number)


even_numbers = [4, 15, 22, 7, 30, 9]
for number in even_numbers:
    if number % 2 == 0:
        print(number)

Numbers = [5, 10, 15, 20, 25]
for number in Numbers:
    if number > 10 and number % 2 == 0:
        print(number)

Shopping = ["bread", "milk", "rice", "egg"]
Shopping.append("chicken")
Shopping.remove("milk")
print(Shopping)
for item in Shopping:
    print(item)

prices = [1000, 2500, 500, 3000, 1500]
for amount in prices:
    if amount > 1000:
        print(amount + 500)

scores = [40, 75, 60, 90, 35]
total = sum(scores)
count = len(scores)
average = total / count
print(min(scores))
print(max(scores))
print(sum(scores))
print(average)