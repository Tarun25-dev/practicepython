# Exception Handling - Exception Handling is used to prevent your program from crashing when an error occurs.
#--> Basic Structure
"""
try:
    # code that might cause an error
except:
    # code that runs if an error happens
"""
#1. Example
a=int(input("enter a value :"))
try:
    x=a/0
except:
    print("a number can't by  zero")

#2. Example - Handling a Specific Exception
try:
    x=int("hello")
except ValueError:
    print("only numbers are allowed")

#3. Multiple except blocks
try:
  num=int(input("enter a number: ")) # give string for exception handling -->if you give correct value then the code goes to the next statement
  value=str(input("enter string: ")) # give number for exception occurs -->if you give correct value then the code goes to the next statement.  
  n=10/0
except ValueError:
    print("only numbers are allowed")
except TypeError:
    print("only strings are allowed")
except ZeroDivisionError:
    print("a number is not divisible by zero")

#4. try – except – else --> else runs only if there is NO error.
n=int(input("enter nominator: "))
d=int(input("enter denominator: "))
try:
    result=n/d
except ZeroDivisionError:
    print("denominator can't be zero")
else:
    print("successfully operation:",result)


#5. try – except – finally -->finally runs no matter what(success or error)
try:
    files=open("nofile.txt",'r')
except FileNotFoundError:
    print("file not found!")
finally:
    print("Execution completed")


#6. Catching all errors just like this keyword using exception but this is not recommended but useful for beginners.
try:
    print(10 / 0)
except Exception as e:
    print("Error:", e)

try:
  files=open("nofile.txt",'r')
except Exception as e:
   print("error:",e)


