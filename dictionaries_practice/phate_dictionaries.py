# A dictionary is a collection of data stored as key-value pairs, 
# where each key is used to access its corresponding value.
student = {
    "name": "Faith",
    "age": 25,
    "course": "AI Engineering"
}
print(student["name"])
print(student["age"])
print(student["course"])

# dictionary[key] = value is used To add something, we use the same idea, but with =:
student["city"] = "Lagos"
print(student)

# Python has a keyword called del. we use it to remove an item from the dictionary.
del student["age"] 
print(student)

# checking whether a key exists python lets us ask: "name" in student
print("name" in student)
# When you use in with a dictionary, Python checks the keys:
# "name" in student      # True
# "Faith" in student     # False

# Python also lets us check whether a value exists using: "Faith" in student.values()
print("Faith" in student.values())
# .values() tells Python “Look through the values of this dictionary.”

# student.keys() which gives you the dictionary's keys.
print(student.keys())

# student.values() which gives you the values.
print(student.values())

# student.items() which gives you the key + value pairs.
print(student.items())