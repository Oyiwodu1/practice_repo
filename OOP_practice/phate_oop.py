# object oriented programming
# An object is something that contains:
# Data — information about it
# Behavior — things it can do

# Class = blueprint
# Object = thing created from the blueprint

# Class → the pathway/plan that tells you how to get somewhere.
# Object → an actual journey/person using that pathway.

# A class is created using the class keyword
class student:
    pass #pass means there's nothing inside the class yet
student1 = student()

# Attribute = what the object has
# Method = what the object can do

# attribute are data/information belonging to an object
# Student → class
# Faith → object
# age, course, hobby → attribute

# A method is a function that belongs to a class/object.

class student:
    def study(self): #anything that comes first in the parenthesis after defining the function in a class. It is a conventional name for the current object.
        print("I am studying")
student1 = student()
student1.study()

# __init__ is a special method that runs when we create a new object.
class pupils:
    def __init__(self, name):   #self is the object while name is the attribute
        self.name = name #Take the name we were given and store it inside this particular object
pupils1 = pupils("Faith")       
pupils2 = pupils("Joy")
print(pupils1.name)
print(pupils2.name)

class Student:
    def __init__(self):
        print("Hello Faith")
student1 = Student()