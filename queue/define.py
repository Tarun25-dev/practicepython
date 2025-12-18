# queue - A queue is a data structure that follows FIFO
# Like a line at a bus stop
# import queue module to use queue datastructure
# Python provides a thread-safe queue in the queue module.
# why we cant iterable(looping) queue object beacuse it is thread safe
from queue import Queue
q=Queue()
# basic structure like: Front → [10, 20, 30] ← Rear
q.put(10)
# if we want to put multiple values fast instead of one by one then we use loops concept
for item in (20,30,40,50,60,70,80,90):
    q.put(item)
q.get() # removes first element which is 10

# if we need to see the items in queue
# what happens means one by one element deleted in stack and at same time one by one item stored in temp list and then again we add values to stack from temp list to stack again
temp=[]
while not q.empty():
    item = q.get()
    print(item)
    temp.append(item)
for item in temp:
    q.put(item)


