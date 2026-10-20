# stack is a data structure that follows LIFO(last in first out)
# Fundamental operations in stack
# push (add an item to the top of the stack)
# pop(remove and return an item from the top of the stack)

stack = []
stack.append("Red")
stack.append("Blue")
stack.append("Green")
first = stack.pop()
print(first)

numbers = [10, 20, 30]
x = numbers.pop()
print(x)

# queue is a data structure that follows FIFO(first in first out)
# Add: append()
# Remove: usually pop(0) for a simple list implementation

queue = []
queue.append("Faith")
queue.append("Joy")
queue.append("Grace")
print(queue.pop(0))

queue = ["Faith", "Joy", "Grace"]
served1 = queue.pop(0)
served2 = queue.pop(0)
print(served)
print(served2)
print(queue)

