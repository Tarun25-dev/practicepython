# math - math is used for mathematical operations

import math as m
print(m.sqrt(16)) #4.0 which give floating if we want conver to int using int()
print(m.pow(2,5)) #32.o
print(m.factorial(4)) #24 
print(m.pi) #3.141592653589793

#sys - it is used for system related info
import sys
print(sys.version) #about python version - 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)
print(sys.argv) #current path - ['E:\\python\\modulesAndPackages\\bultinpackages.py']
sys.stdout.write("tharun kumar") #alternative for  print() but no used regularly

#os - operating system(Used to work with files & folders)
import os
print(os.getcwd()) # Current directory - E:\python
# os.mkdir("pythonTest") #creates a folder named pythonTest
# os.remove("pythonTest") #deletes an existing file

#datetime - Used to work with dates and times
import datetime
now=datetime.datetime.now()
print("current time is :",now) # 2025-12-13 12:18:16.328426
print(now.year) #2025
print(now.day) #13
print(now.month) #12
print(now.strftime("%d-%m-%y")) #13-12-25


# time - Used to pause execution
import time
print("started and i will end exactly in 5 seconds")
time.sleep(5)
print("session ended..")

# random - Used to generate random numbers
import random
rNum=random.randint(1,10)
print(rNum)
cNum=random.choice([10,20,30,40,50,60,70,80,90])
print(cNum)

# statistics - Used for mean, median, etc.
import statistics
data=[1,2,3,4,5,6,7,8]
print("mean of this data is:",statistics.mean(data)) # mean of this data is: 4.5
print("meadian of this data is:",statistics.median(data)) # meadian of this data is: 4.5

# functools - Used for reduce()
import functools as f
li=[1,2,3,4,5,67,8,9]
print(f.reduce(lambda x,y:x+y,li)) #99

# collections - special data types 
# counter - Counts how many times an element appears.
from collections import Counter
li1=[1,2,3,4,5,5,3,2]
print(Counter(li1)) # Counter({2: 2, 3: 2, 5: 2, 1: 1, 4: 1})

#defaultdict - Like dictionary, but avoids KeyError
#instead of writed this
#d={}
#d['a']+=1
#print(d) which gives an error called keyError
from collections import defaultdict 
d=defaultdict(int) #which create an empty dictionary with value as integer
d['a']+=1
print(d) #defaultdict(<class 'int'>, {'a': 1})

#deuqe - Double Ended Queue, Faster than list for adding/removing at both ends.
from collections import deque
dq=deque([1,2,3,4,5,6])
dq.append(7)
dq.appendleft(0)
dq.pop()
dq.popleft()
print(dq) # deque([1, 2, 3, 4, 5, 6])

# namedtuple - Tuple with names instead of index
from collections import namedtuple
student=namedtuple('Student',['name','age'])
s1=student('tharun',22)
s2=student("kumar",23)
print(s1,s2) #Student(name='tharun', age=22) Student(name='kumar', age=23)
print(s1.name) #tharun

# why this instead of tuple
# Cleaner than tuple
# Readable code


