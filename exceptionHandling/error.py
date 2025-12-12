"""
# ERROR - An error means something is WRONG in your code, which can stop your program.
print(10/0) # ZeroDivisionError: division by zero
# Types of errors in python - 2 types

#1. Syntax error - A syntax error happens when your Python code breaks the grammar rules of Python.
# Python cannot understand the code, so it stops immediately before running anything. This error comes from WRONG code structure.

for i in range(10)
   print("tharun") #SyntaxError: expected ':'

#2. Runtime error(Exceptions) - A Runtime Error happens while the program is running.
# Syntax is correct
# Program starts running
# But Python gets some problem during execution

# common examples for runtime errors
#1. ZeroDivisionError - Mathematically, division by zero is undefined. So Python stops your program and throws an exception.
# Simple Example for this error
        #Why is dividing by 0 not possible? (Simple Explanation)
        #Imagine you have 10 chocolates and you want to divide them among:
        #--> 5 people → Each gets 2
        #--> 2 people → Each gets 5
        #--> 1 person → Each gets 10

            # But…

        #--> If you divide among 0 people,
        #--> Who gets the chocolates?
        #--> It's impossible — no one is there to divide.
print(10/0) ## ZeroDivisionError: division by zero

#2. Value Error - When the value type is wrong.
n=int("tharun") #Exception has occurred: ValueError

#3. Type Error - when the data type is wrong
print("age"+22) #Exception has occurred: TypeError beacuse age is a string and 22 is integer then concate only works for strings


#4. Index Error - Index out of range.
a=[1,2,3]
print(a[4]) #IndexError: list index out of range


#5. FileNotFound error - when the file is unavailable even though you are calling file
file=open("nofile.txt",'r') #FileNotFoundError: [Errno 2] No such file or directory: 'nofile.txt'
"""
#-->SUMMARY<--#
# Runtime Error = Occurs while program is running.
# Program starts → Suddenly stops because something went wrong.
# These errors are called EXCEPTIONS.
