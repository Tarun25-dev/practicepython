# Tuple - A tuple is like a list, but cannot be changed (immutable)
# ordered and allow duplicates
# comma is must even though there is single element in tuple
# it is also a datatype in python

t=(1,2,3,4,5)
print(type(t)) #<class 'tuple'>

tu=(1,) #comma must

#accesing tuple elements 
tuple=(1,2,3,5,3,5,4)
print(tuple[0]) #gives first element
print(tuple[-1]) #gives last element

#slicing in tuple same as in list
#slicing - extracting a portion of a list, string, or tuple without modifying the original.
#sequence[start : stop : step]
tp=(9,1,3,4,5,3,2,5)
print(tp[0:7:1])
print(tp[::-1])
