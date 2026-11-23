import numpy as np

numbers = np.array([10, 20, 30])
print(numbers * 2)

# calculating average
scores = np.array([50, 60, 70, 80])
average = np.mean(scores)
print(average)

# calculating sum
scores = np.array([10, 20, 30, 40])
total = np.sum(scores)
print(total)

# finding largest and smallest value
numbers = np.array([12, 45, 8, 67, 23])
print(np.max(numbers))
print(np.min(numbers))


# Function	    Purpose
# np.mean()	    Calculates the average
# np.sum()	    Calculates the total
# np.zeros()	Creates an array of zeros
# np.ones()	    Creates an array of ones
# np.arange()	Creates a range of numbers