"""
Sqrt(x)
Given a non-negative integer x, compute integer square root (ignore decimals).
Example: 8 → 2
"""
n=int(input("Enter number:"))
print(int(n**0.5)) # why 0.5 means actual squareroot value is 1/2 then it is also 0.5

#method 2
import math
print(int(math.sqrt(n)))

#method 3
m=0
while ((m+1)*(m+1))<=n:
    m+=1
print(m)

"""
if n=10
1*1=1 <=10 true m increment 1
2*2=4 <=10 true m increment 1
3*3=9 <=10 true m increment 1
4*4=16 <=10 false exit loop
"""