# a method is an action that belongs to an object
#EXAMPLE
#Shopping.append("rice")  #  append() is a list method because it is an action we can perform on a list.


# .insert(index, value)  .insert() adds a new item and shift others to the right
fruits = ["apple", "orange", "mango"]
fruits.insert(1, "banana")
print(fruits)

# .count() it counts how many times a particular value appears in a list
Fruits = ["apple", "banana", "apple", "orange", "apple"]
print(Fruits.count("apple"))

#  .index() helps you find the position
fruits = ["apple", "mango", "orange"]
print(fruits.index("mango"))

# .extend() it adds list together
fruits = ["apple", "mango"]
more_fruits = ["orange", "banana"]
fruits.extend(more_fruits)
print(fruits)

# .reverse() changes the order of the  list so the last item becomes first.
letters = ["A", "B", "C", "D"]
letters.reverse()
print(letters)
