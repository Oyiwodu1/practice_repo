# Inheritance is an OOP feature where a child class gets the attributes and methods of a parent class.
# Parent class
    #  ↓
#   Child class

# the parent is the class being inherited from
# the child is the class that inherits

class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    pass
dog1 = Dog("Buddy")
print(dog1.name)

class Animal:  #Parent class
    def eat(self): #Inherited method
        print("Eating")

class Lion(Animal): #Child class
    def roar(self):   #lion's method
        print("roarrrr")
lion1 = Lion()
lion1.roar()
lion1.eat()

