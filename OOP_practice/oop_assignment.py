# self → object
# self.name → attribute of the object
# name → parameter

class  student:
    def __init__(self, name, age):   
        self.name = name
        self.age = age
student1 = student("Faith", 25)
print(f"Age: {student1.age}")

# class       → blueprint
# object      → actual thing
# __init__    → sets up a new object
# self        → the particular object
# parameter   → receives information
# argument    → actual information given
# attribute   → information stored in the object
# method      → action the object can perform