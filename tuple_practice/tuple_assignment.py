student = ("Faith", 25, "AI", "Nigeria")
name, age, field, country = student
print(name)
print(field)
print(country)

student_list = list(student)
student_list[1]= 26
student = tuple(student_list)
print(age)
print(student)

colors = ("red", "blue", "green")
colors_list = list(colors)
colors_list[1] = "yellow"
colors = tuple(colors_list)
print(colors)