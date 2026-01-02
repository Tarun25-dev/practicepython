# Use one queue and rotate it every time you push.
# When you push x:
# Add x to the queue
# Move all elements before x to the back
# this makes x come to the front, acting like a stack top
# To implement all stack operations using only queue behavior.
# Stack should work as LIFO (Last In, First Out)
# But you are only allowed to use queues, which work as FIFO (First In, First Out)
import queue
q=queue.Queue()
q.put(10)
q.put(20)
q.put(q.get()) # removes the front element of the queue and returns it.
print(list(q.queue))

q.put(30)
q.put(q.get())
q.put(q.get())
pop_element=q.get()
print(pop_element) #stack behaviour on queue
final=[]
while not q.empty():
    final.append(q.get())
print(final) # [20, 10]
