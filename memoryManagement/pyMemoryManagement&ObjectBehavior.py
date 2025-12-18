# copy concept - Copy means creating another object from an existing one
# But the question is:
# Do they share inner data or not?
# for copying an object we must import copy package
# there are two types of copying an object
# 1. Shallow copy
# 2. Deep copy
# 1. Shallow copy - Creates a new outer object, Inner (nested) objects are shared
# which means if you modify any data inside object it reflects on main object
# we can check whether an object  using same ref or difference references using id(name)
import copy
obj1=[[1,2],
      [4,5]]
obj2=copy.copy(obj1) # shallow copy
print(obj2)
obj2[0][0]=25
print(obj1)

"""
[[1, 2], [4, 5]]
[[25, 2], [4, 5]]
"""

"""
When to use shallow copy
 Data has no nested objects
 You want fast copy
 You don’t care if inner data is shared
"""
# the output shows cause of shallow memory

#2. deep copy - Creates a new outer object, Creates new inner objects also and it is Completely independent
obj3=[["a","b","c"],
      ["e","d","f"]]
obj4=copy.deepcopy(obj3)
obj4[0][1]="c" # which replaces [0][1] value which is "b" into "c"
print(obj3)
print(obj4)
# modifications on copy object cant effect on original object data
"""
[['a', 'b', 'c'], ['e', 'd', 'f']]
[['a', 'c', 'c'], ['e', 'd', 'f']]
"""

# if we find specific object reference to check we use id(name)
# name as any type like list/string/tuple/etc,..
a=[10,20,30,40,50]
b=a # list data shared through reference
b.append(60)
print(a) # [10, 20, 30, 40, 50, 60] beacuse both a and b variables uses reference for same data
print(id(a),id(b)) #same reference like  1601192002064 1601192002064