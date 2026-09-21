student = {
    "name": "Faith",
    "age": 25,
    "course": "AI Engineering"
}
student["city"] = "Lagos"
student["age"] = 26
del student["name"]
for key, value in student.items():
    print(f"{key}: {value}")