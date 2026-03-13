# Sieve - Count all prime numbers from 1 to N.
# Example: N=20 → Primes: 2,3,5,7,11,13,17,19 → Count: 8

N = int(input("Enter N:"))
sieve = [True]*(N+1)
sieve[0]=sieve[1]=False
for i in range(2,int(N**0.5)+1):
    if sieve[i]:
        for j in range(i*i,N+1,i):
            sieve[j]=False
print(sum(sieve))