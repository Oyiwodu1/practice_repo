def my_function(): # function, function name, parenthesis
    print("hello from function")

my_function()
my_function()
my_function()

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(50))

def get_greetings():
    return "hello from my function"
message = get_greetings()
print(message)

def my_func(fname): # fname is a parameter
    print(fname + "praise")
my_func("sing ") # "sing" is an argument in the parameter
my_func("come and ")

def try_func(tname):
    return f"{tname} you"
print(try_func("thank"))
print(try_func("peace"))    

def my_function2(mname, name):
    print(mname + " " + name)
my_function2("come", "here")

def default_func(names = None):  #default parameter value
    print("Hello", names)
default_func("favour")
default_func("faith")    
default_func()

