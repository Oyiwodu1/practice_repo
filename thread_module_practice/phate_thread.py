# threading is a built-in Python module that allows us to create
#  and manage multiple threads within one program.
import threading
import time

def receive_orders():
    print("Receiving customer orders...")
    print(threading.current_thread().name) # checking the thread name
worker = threading.Thread(target=receive_orders, name="OrderReceiver") # name: giving the thread a meaningful name.
worker.start()

# threading.Thread() creates the thread.
# worker.start() starts the thread.
# target=receive_orders tells the thread which function to execute.

def receive_orders():
    print("Receiving orders...")
def process_orders():
    print("Processing orders...")
worker1 = threading.Thread(target=receive_orders, name="OrderReceiver")
worker2 = threading.Thread(target=process_orders)
worker1.start()
worker2.start()



def receive_orders():
    time.sleep(4)
    # time.sleep() pauses the execution of the thread that calls it for a specified number of seconds.
    print("Orders received.")
def prepare_orders():
    time.sleep(7)
    print("Orders prepared.")
worker1 = threading.Thread(target=receive_orders)
worker2 = threading.Thread(target=prepare_orders)

worker1.start()
worker2.start()
worker1.join()
worker2.join()
print("All tasks completed")
# current_thread()
# Python allows us to identify which thread is currently executing a piece of code.
print(threading.current_thread().name)
