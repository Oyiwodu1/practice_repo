class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("eating")
class Lion(Animal):
    def roar(self):
        print("roarrrr")
lion1 = Lion("Simba")
lion1.roar()
print(lion1.name)


# super() is used inside a child class to access things from its parent class.
class Animal():
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name, mane_color):
        super().__init__(name)
        self.mane_color = mane_color
        print(f"My dog's name is {self.name} and it's {self.mane_color} in color")
dog1 = Dog("Wolly", "Black")
print(dog1.name)


