# A set is a collection of unique values.
# Sets use curly braces {}:
fruits = {"apple", "banana", "orange"}

# Sets Don't Keep Duplicates
numbers = {1, 2, 2, 3, 3, 3}
# Python will store: {1, 2, 3}

# A set is mutable, meaning you can add or remove values after creating it.
# names[0] idexing won't work because sets don't use positions like lists.

# we use .add() to add to a value to an extising set
names = {"Faith", "Joy"}
names.add("Peace")
print(names)

# .remove() is used to remove a value from an extising set
animals = {"cat", "dog", "rabbit"}
animals.remove("dog")
print(animals)

# .discard() → simply does nothing if the value isn't there.

#  3 SET OPERATIONS
# set1.union(set2): Union combines the values from both sets, removing duplicates.
A = {"apple", "banana", "orange"}
B = {"banana", "orange", "mango"}
result = A.union(B)
print(result)

# A.intersection(B) Intersection means:What do these two sets have in common?
A = {"apple", "banana", "orange"}
B = {"banana", "orange", "mango"}
result = A.intersection(B)
print(result)

# A.difference(B) Difference asks “What is in the first set that is NOT in the second set?”
A = {"cat", "dog", "rabbit"}
B = {"dog", "rabbit", "lion"}
result = A.difference(B)
result2 = B.difference(A)
print(result)
print(result2)

# A.symmetric_difference(B) means Give me the values that are in either set, but NOT in both.
A = {"apple", "banana", "orange"}
B = {"banana", "orange", "mango"}
result = A.symmetric_difference(B)
print(result)