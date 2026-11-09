#  DEQUEUE => double ended queue
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