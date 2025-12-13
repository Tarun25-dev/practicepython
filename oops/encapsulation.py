# Encapsulation - Hiding data
# Encapsulation means keeping the data (variables) and methods together inside a class and restricting direct access from outside.
# Why Encapsulation?
# Prevents accidental changes to data
# Makes code more secure and maintainable
# Provides controlled access to data

# Public members → fully accessible from outside
# Protected members → single underscore _ (convention)
# Private members → double underscore __ (restricted access)

#1. public members Example
class mydata:
    def __init__(self,name,age):
        self.name=name  #public
        self.age=age    #public
obj1=mydata("Tharun",22)
print(obj1.name)
print(obj1.age)

#2. protected members
class animal:
    def __init__(self,name,type):
        self._name=name  #protected
        self._type=type  #protected
obj2=animal("tiger","non-vegetarian")
print(obj2._name)

# Python uses single underscore _ to mark it as protected
# It’s a convention, not a strict restriction. - A convention is like a rule that everyone agrees to follow, but Python does not enforce it strictly.
# It works, but you are “not supposed to touch it directly”

#3. private members
class liquid:
    def __init__(self,name,color):
        self.__name=name    #private
        self.__color=color  #private
    def get_name(self): # get_name() is a method, We define it to access private/protected data safely this is called getter method
        return self.__name
        
obj3=liquid("milk","white")
print(obj3.get_name()) #milk

# Using Setter to update
class student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,age): # we created a custom method to update the data in object securely called setter method
        if age > 0:
            self.__age = age
        else:
            print("age must be in positive number")
obj4=student("tharun",22)
print(obj4.get_age()) # 22
# update needed then use setter method
obj4.set_age(23)
print(obj4.get_age()) #23

    
