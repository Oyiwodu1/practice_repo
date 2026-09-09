fname = "joy"    #global variable
def multiply_numbers(*args):  #arg(non keyword arguement*; This function can receive any number of positional arguments.")
    result = 5
    for num in args:  # 'args' is a tuple of all inputs
        result = result * num + 2
    return result

print(multiply_numbers(2, 3))      
print(multiply_numbers(2, 3, 4, 5))  

def print_profile(**kwargs):  #kwargs(keyword arguement**; collect keyword arguement into a dictionary)
    result = ", ".join(f"{key}: {value}" for key, value in kwargs.items())
    print(result)
    print(fname)

print_profile(name="Alice", role="Developer")
print_profile(name="Favour", role="engineer")
print_profile(name="Faith", age=20, country="Nigeria")


ggg = " / ".join(["name: Alice", "role: Developer"])  #using the .join keyword to convert multiple string to one string 
print(ggg)

result = ", ".join(["favour", "peace", fname])
print(result)
