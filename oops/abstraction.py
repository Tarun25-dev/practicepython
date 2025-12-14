# Abstrction - Hiding internal details and showing only what is necessary
# You know what to do, You don’t know how it works internally.

# Example in real world: Car
# You know: accelerator, brake, steering
# You DON’T know: engine internal process and fuel combustion logic 

# Why do we need Abstraction?

# --> To reduce complexity
# --> To hide implementation
# --> To force rules
# --> To make code clean & secure

# Python provides 2 ways to acheive abstraction:
# Abstract class   - A class that contains abstract methods
# Abstract method  - A method with no implementation, only declaration
# --> using abc mosule 
# important rule is You cannot create an object of an abstract class

# Python does not have abstract classes by default. So Python gives a special module called abc(Abstract Base Classes
# @abstractmethod - Because just writing pass is NOT enough.
# Without @abstractmethod:
# Child class is NOT forced to implement the method
# Object creation will still work
# With @abstractmethod:
# Child class MUST implement the method
# Otherwise → ERROR

from abc import ABC, abstractmethod
class parent(ABC): # abstract class
    @abstractmethod #It is a decorator, It comes from the abc module, It is used inside abstract classes.
    def sound(self):
        pass # I’m intentionally leaving this empty. Child will fill it.
class child(parent):
    def sound(self):
        print("child implementation")
obj=child()
obj.sound() # child implementation