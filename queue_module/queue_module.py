# join() — waiting for all tasks to finish

import queue

orders = queue.Queue()

orders.put("Rice")
orders.put("Chicken")
orders.put("Fish")

order = orders.get()
print("Preparing:", order)
orders.task_done()

order = orders.get()
print("Preparing:", order)
orders.task_done()

order = orders.get()
print("Preparing:", order)
orders.task_done()

orders.join()
print("All orders completed!")
# Very important: If you retrieve an item using get() but forget to call task_done(), 
# join() may wait forever because Python still considers that task unfinished.
