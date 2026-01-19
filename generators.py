# A generator is a special type of function that returns values one at a time, instead of returning all values at once.
# It is mainly used for save memory
# Work with large data files
# Make program faster and efficient

def nums():
    yield 1
    yield 2
    yield 3
    yield 4
for n in nums():
    print(n)
# this doesnt store all values,it generates them when needed

# There are two ways to create generators
# 1. using yield 
# 2. generator expression

# 1.
def count():
    for i in range(6):
        yield i
for value in count():
    print(value)
    
# 2
gen = (x*x for x in range(5))
for i in gen:
    print(i)