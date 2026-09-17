def greeting():
    def message(name):
        print(f"Welcome {name}")
    return message
result = greeting()
result("Faith")

def double(num):
    return num * 2

def run_operation(double):
    print(double(10))
run_operation(double)   # Passing a function as an argument
