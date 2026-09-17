# Recursion is when a function calls itself.

def count(n):

    if n == 0:   # BASE CASE → tells it when to stop
        return

    print(n)
    count(n - 1)   # RECURSIVE CALL → function calls itself
count(3)
print()

def count():
    print("Hello")
    count()


def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
countdown(5)
print()

def add_down(n):
    if n == 0:
        return 0      # base case / stop
    return n + add_down(n - 1)   
add_down(4)
print(add_down(4))
print()

def print_string(word, index):
    if index == len(word):
        return

    print(word[index])
    print_string(word, index + 1)
print_string("FAITH", 0)