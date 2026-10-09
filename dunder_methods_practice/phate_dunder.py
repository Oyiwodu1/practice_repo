# Dunder means double underscore __init__
# __init__ controls what happens when an object is created
# __str__ contols what happens when python tries to turn your object into a readable string

class Customer:
    def __init__(self, name):  #init what should happen when the object is created
        self.name = name
    def __str__(self): #str, what the object should look like when its printed 
        return self.name
customer1 = Customer("Faith")
print(customer1)

class Dog:
    def __str__(self):
        return "I am a dog"
dog = Dog()
print(dog)

# __len__ controls what len(object) returns

class Team:
    def __init__(self, members):
        self.members = members
    def __len__(self):
        return len(self.members)
team = Team(["Faith", "Joy", "Peace"])
print(len(team))

# __repr__ representing an object / gives useful representation of the object 

class Company:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Company(name='{self.name}')"
worker = Company("Joy")
print(worker)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __repr__(self):
        return f"Book(title = {self.title}, author = {self.author})"
book = Book("Things fall Apart", "Chinua Achebe")
print(repr(book))

# __eq__ equal : controls what happens when we use == between objects
# object1 == object2

class Customer:
    def __init__(self, name):
        self.name = name 
    def __eq__(self, other):
        return self.name == other.name
customer1 = Customer("Faith")
customer2 = Customer("faith")
print(customer1 == customer2)

# __add__ lets you decide what + means for your object / object1 + object2

class Money:
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, other):
        return self.amount + other.amount
money1 = Money(4000)
money2 = Money(900)
print(money1 + money2)

# __lt__ controls < between objects / object1 < object2

class Student:
    def __init__(self, score):
        self.score = score
    def __lt__(self, other):
        return self.score < other.score
student1 = Student(20)
student2 = Student(50)
print(student1 < student2)

# __gt__ controls > between objects / object1 > object2

class Student:
    def __init__(self, score):
        self.score = score
    def __gt__(self, other):
        return self.score > other.score
student1 = Student(60)
student2 = Student(20)
print(student1 > student2)

# __le__ controls <= between objects / object1 <= object2

class Student:
    def __init__(self, score):
        self.score = score
    def __le__(self, other):
        return self.score <= other.score
student1 = Student(20)
student2 = Student(76)
print(student2 <= student1)

# __ne__ not equal to / object1 != object2

class Student:
    def __init__(self, score):
        self.score = score
    def __ne__(self, other):
        return self.score != other.score
student1 = Student(8)
student2 = Student(0)
print(student1 != student2)