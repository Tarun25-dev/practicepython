# two types of scope 
#1. local scope -- A variable created inside a function belongs to that function only.
#2. global scope -- A variable created outside any function is global.

y=20 #global variable
def main():
    x=10  #local variable
    y=30  #local variable
    print(x+y)
main()