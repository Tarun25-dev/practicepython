""" Happy Number
A number is happy if repeatedly summing squares of digits ends in 1.
Return true if happy, else false.
"""
number=int(input("Enter a number:"))
slow=number
fast=number

def happy(x):
    s=0
    while x>0:
        d=x%10
        s=s+d*d
        x//=10
    return s

while True:
    slow=happy(slow)
    fast=happy(happy(fast))
    if fast==1:
        print("Happy!")
        break
    if slow==fast:
        print("Not happy")
        break


    