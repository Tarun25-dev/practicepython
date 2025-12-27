"""
 Fizz Buzz
Given n, print numbers from 1 to n.
Multiple of 3 → "Fizz"
Multiple of 5 → "Buzz"
Multiple of both → "FizzBuzz"
"""

n=int(input("enter a number:"))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print(i,"FizzBuzz")
    elif i%3==0:
        print(i,"Fizz")
    elif i%5==0:
        print(i,"Buzz")
    else:
        print(i)
   
    