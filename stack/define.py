# stack - a stack is a LIFO datastructures
# Think of a stack of plates - the last plate you put on top is the first one you remove. 
# Ways to Implement Stack in Python:
# 1. using list
stack = []
stack.append(10) # acts a push 
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
# this works same like adding first element goes to first place and last element placed at last
stack.pop() # acts as pop - removes top of the stack
stack.pop()
print(stack[-1]) #30  acts as peek - means it shows top element of the stack, it just observing that top element but this not be delete the element like pop
# this works same like adding last element that removes first using pop()
print(stack) #[10, 20, 30]
# this is not thread safe (beacuse we cant add/insert multiple values in list at a time) but i still not go that level to understand this threadening concept

#2. Using collections.deque
from collections import deque
stk=deque()  # Create a stack object using deque class and stack is now an empty stack.
stk.append(10)
stk.append(20)
stk.append(30)
stk.pop()
print(stk)
print(type(stk)) # <class 'collections.deque'>
# faster than python list
# Safer for multi-thread use (atomic operations) still learning this concept 

#3. Using queue.LifoQueue (Thread-safe stack)
from queue import LifoQueue
st=LifoQueue() # Create a thread-safe stack object using lifoqueue class and stack is now an empty stack.
st.put(10)
st.put(20)
st.put(30)
st.put(40)
st.get() # removes top most element in stack just like as pop()
print(st.empty()) # checks stack is empty or not through True/False #False
# we dont have any method like peek but we can do this for that value
top=st.get() # this removes top element and also stored in top variable of that value.
print(top) #30
st.put(top) # again we need to place that removed value beacuse peek method only observes the value not to be remove
print(st.qsize()) # this returns stack size length #3

# print(st) -only shows object references, This does NOT show elements, because LifoQueue hides its data internally for thread safety.
# follow this method for accessing stack safe way 

st1 = LifoQueue()
st1.put(1)
st1.put(2)
st1.put(3)

temp = []

while not st1.empty():
    item = st1.get()
    print(item)
    temp.append(item)

# restore stack
for item in temp:
    st1.put(item)
# what happens means one by one element deleted in stack and at same time one by one item stored in temp list and then again we add values to stack from temp list to stack again
