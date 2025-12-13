# Inheritence - One class uses the properties and methods of another class(Just like child inherits properties from parents)
# Why Inheritance?
# --> Avoids code duplication
# --> Improves reusability
# --> Makes code clean and organized

class animal:
    def eat(self):
        print("animal eats food")
class dog(animal): # child class, Dog inherits Animal
    def bark(self):
        print("dog is barking")
d=dog() # created object
d.bark() # dog is barking - this is dog method then no problem beacuse we use object for that method
d.eat() # animal eats food - this is eat method we cant call the eat method directly but we access though inheritence by using this line of code "class child(parent):"

# Types of inheritence:

#1. single inheritence - A child class inherits from one parent class(Parent → Child)
class A:
    def show(self):
        print("Class A")

class B(A):
    pass

#2. multilevel inheritence - A class is derived from a class which is already derived from another class(Grandparent → Parent → Child)
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(B):
    def showC(self):
        print("Class C")

c = C()
c.showA()
c.showB()
c.showC()

#3. Multiple Inheritance - A child class inherits from more than one parent class(one child - multiple parents)
class A:                  # parent1
    def showA(self):
        print("Class A")

class B:                  # parent2
    def showB(self):
        print("Class B")

class C(A, B):            # child
    pass

c = C()
c.showA()
c.showB()

#4. Hierarchical Inheritance Multiple child classes inherit from the same parent class(multiple child - one parent)
class A:
    def show(self):
        print("Class A")

class B(A):
    pass

class C(A):
    pass

b = B()
c = C()
b.show()
c.show()

#5. Hybrid Inheritance - Combination of two or more types of inheritance.
class A:
    pass

class B(A):
    pass

class C:
    pass

class D(B, C):
    pass
#this example uses two types of inheritence(single,multiple) thats why it is called as hybrid inheritence


