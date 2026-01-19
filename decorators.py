# DECORATORS - A function that modifies another function without changing its code.
# Its like putting a filter or wrapper around a function
#  we declare decorator like this @function_name also as decorator name 

def decorator(func): # this function takes a parameter as func we call it to the original function like say_hello
    def wrapper():
        print("Good Morning!")
        func() # calling that say_hello function
        print("Have a nice day")
    return wrapper
    
    
# for example we have a hello function like this 
@decorator
def say_hello():
    print("Hello")
# Now we dont want only hello incl.this we need to add some content like good morning

say_hello()