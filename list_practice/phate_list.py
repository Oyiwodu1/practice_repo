# A list is a collection of multiple values stored together in one variable.
fruits = ["Apple", "Mango", "orange", "Grape", "Guava"]
# the individual things inside the list are called elements

fruits[0] = "Banana"  # The ability to change  element is called mutability
fruits.append("watermelon")  # .append() helps us to add an element at the end of the list
fruits.remove("Mango")   # .remove() helps to remove an element by value
fruits.pop(0)   # .pop() removes an item acording to the index number

# .sort() rearranges the list into ascending order — smallest to largest.
fruits.sort() 
print(fruits)
for fruit in fruits:
    print(fruit)



# fruits[1:4]   list[start:stop]       slicing
# numbers[:3]   Start from index 0, stop before index 3.
# numbers[3:]    Start at index 3, continue to the end.

# numbers[::2]   list[start:stop:step] move two positions at a time.
# numbers[::-1]   -1 means returning the list in reverse order.

numbers = [30, 10, 50, 20, 40]
numbers.sort(reverse=True) #  → largest → smallest
print(numbers)



numbers = [5, 12, 7, 20, 3, 18]
for number in numbers:
    if number > 10:
        print(number * 2)

