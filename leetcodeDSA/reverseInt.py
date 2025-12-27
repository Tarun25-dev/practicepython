"""
Reverse Integer
Given a signed 32-bit integer, reverse its digits.
If reversing causes overflow, return 0.
Example: 123 → 321, -120 → -21

"""

maxInt=2**31-1
minInt=-2**31
n=int(input("Enter number"))
sign=-1 if n<0 else 1
reverse=0
temp=abs(n) # neg sign removes
while temp>0:
    d=temp%10
    reverse=reverse*10+d
    temp=temp//10
reverse=reverse*sign #original sign adds
if reverse>maxInt or reverse<minInt:
    print("not a 32bit integer range")
else:
    print("reverse number is:",reverse)

# in python integers start with zeros will take only valid numbers like 001230 is considered as 1230 