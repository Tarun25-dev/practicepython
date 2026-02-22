# sys.stdin - is used to retrive input from the user(standard input)
# it is the input stream connected to keyboard by default

# Normal input 
name = input("Enter Name: ")
# this internally uses sys.stdin
# It reads input line by line.
import sys
data = sys.stdin.readline() # reads one line from input
print("Your data:",data)

# if we want to write enterdata then use write method
sys.stdout.write("Enter Data")
d = sys.stdin.readline()
print("your data",d)
