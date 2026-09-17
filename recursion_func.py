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