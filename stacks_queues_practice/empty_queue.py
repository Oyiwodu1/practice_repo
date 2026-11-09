# Handling empty Queue

queue = []
if queue:
    person = queue.pop(0)
    print(person)
else:
    print("The queue is empty.")
print(bool(queue))

queues = ["Ada", "John", "Grace"]
if queues:
    served_person = queues.pop(0)
    print(served_person)
else:
    print("The queue is empty")

# Finding the length of a queue
queue1 = ["Faith", "Joy", "Grace"]
print(len(queue1))
if len(queue1) > 0:
    print("People are waiting")
else:
    print("Nobody is waiting")

# Setting the maximum size of a queue
queue2 = ["Faith", "Ada", "John"]
maximum_size = 5

if len(queue2) < maximum_size:
    queue2.append("Grace")
    print("Person added successfully")
    print(queue2)
else:
    print("Queue is full")