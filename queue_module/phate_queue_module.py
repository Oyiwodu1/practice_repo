# Python's queue module provides ready-made queue structures for managing items in the order they should be processed.

import queue
# Adding items using put()
customers = queue.Queue()
customers.put("Ada")
customers.put("John")
customers.put("Faith")
print(customers.queue)
print(customers.qsize()) # geting the length of a queue


# Removing items using get()
customer1 = queue.Queue()
customer1.put("David")
customer1.put("Mary")
customer1.put("Peter")
first = customer1.get()
print(first)

# Checking if a Queue is empty using .empty()
customers = queue.Queue()
print(customers.empty())

customers = queue.Queue()
customers.put("John")
customers.put("Faith")
customers.get()
print(customers.empty())

# task_done() — telling Python a task is finished
orders = queue.Queue()
orders.put("Rice")
orders.put("Chicken")
orders.put("Fish")
order = orders.get()
print(order)
orders.task_done()


# Handling an empty queue
customers = queue.Queue()
try:
    customer = customers.get_nowait()
    print(customer)
except queue.Empty:
    print("No customers are waiting.")