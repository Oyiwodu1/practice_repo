def my_function(animal, name):
    print("i have a", animal, end=". ")
    print("My", animal + "'s name is", name)
my_function("dog", "Buddy")
my_function("cat", "Buddy")

def my_function(fruits):
    for fruit in fruits:
        print(fruit)
my_function(["banana"])

def my_function(person): #sending dictionary as set of argument
    print("Name:", person["name"])
    print("Age:", person["age"])
my_person = {"name": "Emil", "age": 25}
my_function(my_person)

def my_function(x, y):
  return x + y
result = my_function(5, 3)
print(result) 


def my_function():  #returns a list
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[1], end=", ")
print(fruits[1], end=", ")
print(fruits[0])

