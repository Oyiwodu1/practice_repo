# when you loop through a dictionary python gives you the key by default
student = {
    "name": "Faith",
    "age": 25,
    "course": "AI Engineering"
}
for item in student:
    print(item)

# using .values() to loop through the values directly
for item in student.values():
    print(item)

# using .items() to get both key and value together
for item in student.items():
    print(item)
