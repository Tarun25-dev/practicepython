"""
Count Primes
Given n, count how many prime numbers are less than n.
Example: n = 10 → 4 (2,3,5,7)
"""
li=[]
n=int(input("enter a number:"))
count=0
for i in range(2,n+1):
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        li.append(i)
        count+=1
print(tuple(li))   
    
