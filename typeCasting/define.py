# Type casting - converting one data type into another.
# Python has two types of casting:
#1. Implicit Casting (automatic)
#2. Explicit Casting (manual)

#1. Implicit casting - Python automatically converts a smaller type to bigger type.
a=10
b=4.5
d=True
c=a+b
print(c,type(c)) #converts int to float 
print(a+d,type(a+d)) # 11 beacuse True value in py is 1 and also the type of bool + int always int
#preference : float > int > bool

#2. Explicit casting - we convert the type yourself using Python functions:
#--> convert to integer
e="10"
f=int(e)
print(type(e),type(f)) #<class 'str'> <class 'int'>

#-->convert to float
g="10.5"
h=float(g)
print(type(g),type(h)) #<class 'str'> <class 'float'>

#-->convert to string
i=25
j=str(i)
print(type(i),type(j)) #<class 'int'> <class 'str'>

#-->convert to list, tuple, set
name="THARUN"
listName=list(name)
tupleName=tuple(name)
setName=set(name)
print(f"{listName}\n{tupleName}\n{setName}")

#-->converting float to int removes the decimal value
#-->you can't convert string(more than one letter) to int