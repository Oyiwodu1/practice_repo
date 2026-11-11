#  DEQUE => double ended queue
from collections import deque

queue = deque(["Faith", "Ada", "John"])
queue.popleft()
queue.appendleft("Favour")
queue.append("Grace")
print(queue)

print()
tasks = deque(["Send email", "Print report", "Save file"])
for task in tasks:
    print("Processing:", task)

print()
queue1 = deque(["Ada", "John", "Grace"])
while queue1:
    customer = queue1.popleft()
    print("Now serving:", customer)

print()
# Extend => adds mutiple items 
queue2 = deque(["Ada", "John"])
queue2.extend(["Faith", "Grace"]) 
print(queue2)

print()
# clear() — emptying a queue - It does not delete the queue variable.
# - The queue still exists, but it is empty.
# - You can add new items to it afterward.
queue = deque(["Ada", "John", "Faith"])
queue.clear()
print(queue)
queue.append("Grace")
print(queue)

print()
# count() — counting occurrences. how many times a particular item appears
queue = deque(["Ada", "John", "Ada", "Faith", "Ada"])
print(queue.count("Ada"))

print()
# remove() — removing a specific item and if there's any duplicate, it removes the first occurrence
queue = deque(["Ada", "John", "Faith", "Grace", "John"])
queue.remove("John")
print(queue)

print()
# rotate() — moves items from one end of the deque to the other
queue = deque(["Ada", "John", "Faith", "Grace"])
queue.rotate(2) #A positive rotation moves items from the right (back) to the left (front).
print(queue)
queue = deque(["Ada", "John", "Faith", "Grace"])
queue.rotate(-1)
print(queue)

print()
# : maxlen — setting a maximum queue size
queue = deque(maxlen=3)
queue.append("Ada")
queue.append("John")
queue.append("Faith")
queue.append("Grace")
print(queue)