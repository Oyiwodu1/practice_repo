def say_hello(name):
    print(f"Hello {name}")
greeting = say_hello
greeting("Faith")  #treating function as first-class object

def say_goodbye(name):
    print(f"Goodbye {name}")
say_goodbye("Faith")


def run_function(greeting):
    greeting("Favour")
run_function(greeting)  #high-order function

#  A higher-order function is a function that takes 
#  another function as an argument or returns a function

