# In Python: no StringBuilder is needed, Because strings are immutable, we don't modify a string directly.
# But Python gives efficient alternatives:

#1. Use LIST + join() → Python’s StringBuilder:
li=["tharun","kumar","kodiganti"]
print(" ".join(li)) 

#2. Use io.StringIO (advanced)
from io import StringIO
string=StringIO()
string.write("tharun")
string.write(" ")
string.write("kumar")
print(string) # you printed the StringIO object itself, not its content.(<_io.StringIO object at 0x000002B5C39FCDC0>)
# if you want content inside use getvalue()
print(string.getvalue()) # tharun kumar

#3. Use += for small strings
s=""
print(id(s)) #2628293722160 (memory address of a string which is empty string we created)
s+="hello "
print(id(s)) #2628332667824 (memory address of a string which is "hello " string we created)
s+="world" 
print(id(s)) #2628341503408 (memory address of a string which is "world" string we created)
print(s) #hello world

# What actually happens internally:
# "hello" stays unchanged
# Python creates a new string "hello world"
# The variable s now points to this new string
# proof is that the stored memory address and we can get that using id(strname)
