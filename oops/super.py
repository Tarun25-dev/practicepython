# Super() keyword - To access parent class methods/constructor from child class.
# Why super() is needed?
# Child class inherits parent, Child has its own constructor/method But you still want parent’s constructor/method values.

class parent:
    def sum(self):
        print("parent property")
class child(parent):
    def sum(self):
        print("child property")
        super().sum()
# super() works only inside a class, not in normal code.
obj=child()
obj.sum() # child property

# Tasks
# call first parent class before child class

class p:
    def sub(self):
        print("parent class called.")
class c(p):
    def sub(self):
        super().sub() # this executes first
        print("child class called.") # and then second this
ob=c()
ob.sub()

# output
# parent class called.
# child class called.

# Call parent constructor from child constructor.
class person:
    def __init__(self,name):
        print("person name:",name)
class student(person):
    def __init__(self, name, age):
        super().__init__("tharun")
        print("age:",age)
objt=student("tharun",22)

# output :
# Person name: Tharun
# Roll number: 101

# Child overrides method but still uses parent logic.
class vehicle:
    def start(self):
        print("vehicle started")
class bike(vehicle):
    def start(self):
        super().start()
        print("bike started")
b=bike()
b.start()

# output:
# vehicle started
# bike started

