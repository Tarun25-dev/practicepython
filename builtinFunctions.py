#1. map() - map() takes each element from a list and transforms it.
# Syntax - map(function, iterable)
# function - decides whether to keep the element (True) or reject (False)
# iterable - list, tuple, string, etc.
# main differ from other fun is - Transform every element

li=[1,2,3,4,5]
def square(n):
    return n*n
result=map(square,li)
print(result) #It returns a map object, we need to convert into a list
print(list(result)) # [1, 4, 9, 16, 25]

#task -- Convert a list of strings to integers using map()
lite=["1","2","3","4","5"]
print(type(lite[0])) #<class 'str'>
def fun(n):
    return int(n)
rt=map(fun,lite)
re=list(rt)
for i in re:
    print(type(i)) #<class 'int'>

# Filter() - filter() is a Python built-in function that is used to select only the elements that satisfy a condition.
# It does not modify the list.
# It checks each element one by one and keeps only true ones.
# syntax - filter(function, iterable)
# main differ from others fun is - Select elements based on condition
numbers=[1,2,3,4,5,6]
def even(n):
    return n%2==0 # which returns true if satisfies else false returns
f=filter(even,numbers)
print(list(f)) #[2, 4, 6]

#for odds 
t=[1,2,3,4,5,6]
def odd(n):
    return n%2!=0 # which returns true if satisfies else false returns
fil=filter(odd,t)
print(list(fil)) # [1, 3, 5]


#3. reduce() - reduce() is used to apply a function to a list, repeatedly, and reduce it to a single value.
# Input list → one final result
# Size becomes 1
# Used for aggregation (sum, product, max, min, etc.)
# find sum of elements in list
from functools import reduce
elements=[1,2,3,4,5,6,7,8,9]
def sum(n1,n2):
    return n1+n2
s=reduce(sum,elements)
print(s) # 45



