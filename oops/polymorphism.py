# Polymorphism - poly = many and morphism = form 
# The same method name behaves differently in different situations.
# Example:
# At home → Father
# At office → Employee
# At college → Student
# Same person, different roles.

# polymorphism has two main types :
#1. method overriding
#2. method overloading

#1. Method overriding - Child class provides its own implementation of a method that already exists in the parent class.

class animal:
    def sound(self):
        print("animal makes a sound")
class dog(animal):
    def sound(self):
        print("dog is barking")
class cat(animal):
    def sound(self):
        print("Meowwwww!")
a=animal() # obj a created 
b=dog() # obj b created
c=cat() # obj c created
# same method calling but different behavior
a.sound() # animal makes a sound
b.sound() # dog is barking
c.sound() # Meowwwww!

# Why overriding happens ? - python checks child class first and then parent class 
# This is called Method Resolution Order (MRO).

# 2. Method overloading - Python does NOT support traditional overloading like Java.
# But we achieve it using:
# Default arguments
# *args
# Multiple methods with the SAME name but DIFFERENT parameters is called method overloading
# example:
# add(int a, int b)
# add(int a, int b, int c)
# Same method name add,
# Different number/type of parameters. 
# python checks parameters when you call add function if that has two parameters then it performs first method else it perform second method
# For method overloading to exist, methods must differ in at least ONE of these:
# Number of parameters
# Type of parameters
# Order of parameters (sometimes)
# for example 
# add(int a , int b)
# add(int a , int b)
# in this example Python does not even try to overload.
# Second add() overwrites the first
# Only one method exists

class test:
    def add(self,a,b):
        print("first method output",a+b)
    def add(self,a,b):
        print("second method output",a*b)
obj=test()
obj.add(2,3) # second method output 6

# even though you take above example with different parameters it also overwrite same way and behaves child method only
# thats why we use default arguments or *args 

# Why Python Does NOT Support Traditional Overloading beacuse,
# Python does not care about parameter types or count at compile time.
# Dynamically typed
# Interpreted at runtime 

# Method overloading with default argument
# A function parameter that already has a value, If you don’t pass a value → Python uses the default one
class g:
    def greet(self,name="hello"): #default value as hello, if you dont give any value while calling this method then it uses that default value
        print(name)
o=g()
o.greet() # hello
o.greet("Hi") # Hi - beacuse it overwrite the default argument value and takes this argument

# Method overloading with multiple default arguments
class gt:
    def gr(self,a,b=0,c=0):
        print("sum is:",a+b+c)
ob=gt()
ob.gr(10)       # sum is: 10
ob.gr(10,20)    # sum is: 30
ob.gr(10,20,30) # sum is: 60

# same method if you pass one arg then remainig takes from default arg same like that here happens
# important rule to follow while working with multiple default arguments
# Default arguments must come after non-default arguments
# example :
# sum(a=0,b=9,c) which is wrong
# sum(c,a=0,b=9) which is correct    

# *args means we can pass no.of arguments at method calling time if you place that in method and also we need to follow one rule which is if you expect must arguments that declared in method should come first after you place that *args
# example:
# * refers to multiple values
# args refers to the argumment name which is custom 
# sum(self,*nums,a,b) # worng
# sum(self,a,b,*nums) # correct

class calculator:
    def sum(self,*nums):
        total=0
        for i in nums:
            total+=i
        print("total sum is:",total)
objt=calculator()
objt.sum(10,20) # total sum is: 30
objt.sum(10,20,30) # total sum is: 60
objt.sum(10,20,30,40) # total sum is: 100
objt.sum(10,20,30,40,50) # total sum is: 150
objt.sum(10,20,30,40,50,60) # total sum is: 210
objt.sum(10,20,30,40,50,60,70) # total sum is: 280
objt.sum(10,20,30,40,50,60,70,80) # total sum is: 360