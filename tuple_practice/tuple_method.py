# .count() it counts how many times a particular value appears 
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))

# .index() tells you the first position of a value
numbers = (10, 20, 30)
print(numbers.index(20))

fruits = ("apple", "mango", "apple", "orange", "apple")
print(fruits.count("apple"))
print(fruits.index("orange"))

# UNPACKING A TUPLE
person = ("Faith", 25, "Nigeria")
name, age, country = person  
print(name)
print(age)
print(country)
