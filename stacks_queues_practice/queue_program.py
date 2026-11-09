queue = []

queue.append("Faith")
queue.append("Peace")
queue.append("Joy")

print("Waiting customers:", queue)
print("Number of customers:",len(queue))
if queue:
    served1 = queue.pop(0)
    print("Now serving:", served1)
print("Remaining customers:", queue)