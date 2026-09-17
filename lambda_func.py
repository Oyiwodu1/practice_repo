 # A lambda function is a small function that doesn't need a traditional name.
 # lambda is a way of creating a small function in one line

result = lambda num: num * 2
print(result(10))

def run_operation(operation):
    print(operation(5))
run_operation(lambda num: num * 2)

# lambda     → tells Python we're making a lambda
# num        → parameter
# :          → separates the parameter from the operation
# num * 2    → expression/result

square = lambda num: num * num
print(square(10))

get_length = lambda word: len(word)
print(get_length("Faith"))

greet = lambda name: "Welcome " + name
print(greet("Faith"))

make_upper = lambda word: word.upper()
print(make_upper("faith"))