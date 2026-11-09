#  DEQUEUE => double ended queue
from collections import deque

queue = deque(["Faith", "Ada", "John"])

queue.popleft()
queue.appendleft("Favour")

print(queue)