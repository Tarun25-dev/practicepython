# oops - object oriented programming language system
# Programming languages provide a system
# That system includes:
# Classes, Objects, Inheritance, Polymorphism, Encapsulation, Abstraction.
# def : OOPS is a programming approach that organizes code into objects containing data and behavior. 
# Example: 
# Car
# --> Data = color, brand, speed
# --> Actions = drive(), brake(), stop()

# CLASS : A class is a blueprint / design / template for creating an object.
# Class doesnt take memory until an object is created.
# it defines : 
# --> what data an object will have
# --> what actions it can perform

# instance - One real object made from that class
# object - An object is a real instance created from a class.
# object takes memory
# using one class we build many objects 

# Example:
# Class --> House plan
# Object --> Actual house (using that house plan we build a house which is called instance)

# creating a class by using keyword class with className.
class car:
    pass

# creating an object
s1=car()

# constructor - A constructor is a special method used to initialize an object when it is created.
# Why do we need a constructor?
# To give initial values to an object.
# Think like this: When a baby is born, we give: name, age
# Constructor does the same for objects.
# Constructor in Python = __init__

class baby: #Class is defined (no output)
    def __init__(self): #Constructor is defined (still no output)
        print("object is created") 
s2=baby() #THIS LINE causes the output
# Python does internally: baby.__init__(s2)
# Object is created
# __init__ runs
# print("object is created") executes
# You did not call print() directly,but you called the constructor indirectly by writing: baby()

# self - self is used to refer to the current object (self tells Python: “this data (instance variables and methods.) belongs to THIS object”)
# Without self, Python throws error
# Object data must be stored using self
# self must be the first parameter
# Object creation parameters → constructor mandatory
# Method parameters → constructor not needed 

# Examples for object creation parameters:
class student1:
    def __init__(self,name): #constructor expects exactly one para called name 
        self.name=name
s2=student1("tarun") #parameter passed during object creation
print(s2.name) #tarun


class student:
    def __init__(self):
        self.name="tharun"
s1=student()
print(s1.name) #tarun

# Example for method parameters 
class bike:
    def method(self,bName):
        self.bName=bName
obj1=bike() #created object
obj1.method("Triumph") #passing argument
obj2=bike()
obj2.method("Yamaha")
print(obj1.bName) # Triumph
print(obj2.bName) # Yamaha

