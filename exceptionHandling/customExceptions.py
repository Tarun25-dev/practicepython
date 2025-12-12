# custom exceptions are also called as built-in errors in python
# Why we use class in custom exceptions,Because every exception in Python is an object
# Python exceptions (like ValueError, ZeroDivisionError, etc.) are classes.
# When an error happens, Python creates an object of that class and raises it.

#Example:
#ValueError --> a class
#ZeroDivisionError --> a class
#FileNotFoundError --> a class

class EmptyInputError(Exception):
    pass
class WeakPasswordError(Exception):
    pass
try:
  username=input("Enter your Name: ")
  password=input("Enter your password: ")
  if username.strip()=="": #strip method removes spaces if user give spaces.
     raise EmptyInputError("username cannot be Empty!")
  if password=="":
     raise EmptyInputError("password cannot be Empty")
  if len(password)<6:
     raise WeakPasswordError("password is too Weak!")
  print("login successfull")
except EmptyInputError as e:
   print("ERROR: ",e)
except WeakPasswordError as w:
   print("ERROR: ",w)