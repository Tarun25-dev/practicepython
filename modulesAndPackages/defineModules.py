# Module - is a python file saved with .py extension
# thar file contain variables,functions and classes
# why modules / packages
#--> Code resuablility
#--> Clean & organized code
#--> Easy debugging
 
import moduleSumfun
moduleSumfun.sum(10,20) #30

#also import specific funvtions from module
from moduleSumfun import sub
sub(20,10) #10

# import with alias name 
import moduleSumfun as s
s.mul(2,5) #10

import moduleSumfun as f
a=int(input("enter a :"))
b=int(input("enter b : "))
f.sum(a,b)
f.sub(a,b)
f.mul(a,b)
f.div(a,b)

# __pycache__ directory: 
# __pycache__ stores compiled .pyc files for faster execution
# It is mostly created for imported modules, but not limited to them
# You write code in .py file
# Python compiles it into bytecode
# That bytecode is saved in __pycache__
# Next run → Python uses it → faster execution
# Example:
# Python compiles modulesSumfun.py
# Stores bytecode in __pycache__/modulesSumfun.cpython-311.pyc 