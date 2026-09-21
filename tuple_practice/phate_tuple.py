# A tuple can store multiple values, just like a list, but a tuple is immutable — meaning you cannot change its contents after it has been created.
# tuple syntax ()

# For a one-item tuple, you need a comma:
a = ("Faith")          # string
b = ("Faith",)        # tuple
c = ("Faith", "Joy")  # tuple

# Because tuples are immutable:
# animals[1] = "lion"
# ❌ Not allowed.   

# But you can still:
# access items ✅
# use negative indexing ✅
# slice them ✅
# loop through them ✅
# use len() ✅
# use methods that don't change them ✅

numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])
print(numbers[-3:])
print(len(numbers))
for number in numbers:
    print(number)