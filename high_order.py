def say_hello(name):
    print(f"Hello {name}")
greeting = say_hello
greeting("Faith")  #treating function as first-class object

def say_goodbye(name):
    print(f"Goodbye {name}")
say_goodbye("Faith")


def run_function(say_goodbye):
    say_goodbye("Favour")
run_function(say_goodbye)  #high-order function

#  A higher-order function is a function that takes 
#  another function as an argument or returns a function

def outer():
    def inner():
        print("Hello Faith")
    return inner
result = outer()
result()    # A function returns another function