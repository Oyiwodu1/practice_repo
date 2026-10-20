a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)

items = []
if items:
    print("There are items")
else:
    print("The list is empty")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

numbers = [10, 20, 30]
numbers.append(40)
removed = numbers.pop()
print(numbers)
print(removed)

my_list = [10, 20, 30]
my_tuple = (10, 20, 30)
my_list[0] = 99
print(my_list)

numbers = {1, 2, 2, 3, 3, 3}
print(len(numbers))

def square(n):
    return n * n
print(square(4))

class Animal:
    def eat(self):
        print("Eating")
class Dog(Animal):
    pass
my_dog = Dog()
my_dog.eat()

class Animal:
    def __init__(self):
        print("Animal created")
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog created")
my_dog = Dog()

print(isinstance(True, int))

student = {"name": "Faith", "age": 20}
print("name" in student)
print("Faith" in student)

def greet(name="Friend"):
    print("Hello", name)
greet()
greet("Faith")

message = "Outside"
def show_message():
    message = "Inside"
    print(message)
show_message()
print(message)

fruits = ["Apple", "Mango", "Orange"]
for index, fruit in enumerate(fruits):  #enumerate() gives you both the index and the item
    print(index, fruit)

names = ["Ada", "Joy", "Faith"]
scores = [80, 90, 95]
for name, score in zip(names, scores): #zip() pairs items at matching positions in the lists: first with first
    print(name, score)

try:
    number = int("hello")
    print(number)
except ValueError:
    print("Invalid number")

name = "Faith"
print(name[0])

x = 10
y = "10"
print(x == y)

def show_info(*args, **kwargs):
    print(args)
    print(kwargs)
show_info("Faith", 20, city="Abuja")

queue = ["A", "B", "C", "D"]
first = queue.pop(0)
second = queue.pop(0)
print(first)
print(second)
print(queue)

queue = ["Ada", "John"]
queue.append("Grace")
first = queue.pop(0)
queue.append("Faith")
print(first)
print(queue)

queue = ["Ada", "John", "Grace"]
person = queue[0]
queue.pop(0)
queue.append("Faith")
print(person)
print(queue)
print(len(queue))