"""n=int(input("Enter a number"))
is_powerOfTwo=False
a=1
while 2**a<=n:
    if 2**a==n:
       is_powerOfTwo=True
       break
    a+=1
print(is_powerOfTwo)

# method 2
n=int(input("Enter a number:"))
is_power=True
if n<=0:
    is_power=False
else:
    while n>1:
        if n%2!=0:
            is_power=False
            break
        n=n//2
print(is_power)  
"""
#method 2
num=int(input("Enter number:"))
b=bin(num)
is_powerOfTwo=False
if num>0 and b.count('1')==1:
    is_powerOfTwo=True
print(is_powerOfTwo)
           

