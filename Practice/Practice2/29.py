# sieve list of prime numbers upto n
# assume all numbers are prime 
# strat from 2
# mark all multiples of 2 as not prime
# move to the next unmarkws number 3
# mark multiples of 3
# why 2,3 only beacuse 2 is the smallest prime and 3 is the next prime
# the sieve removes multipkes of each prime

n = 20
prime = [True]*(n+1) # we need to take upto n from 0 to n so thats why we add +1
for i in range(2,n+1):
    if prime[i]:
        for j in range(i*2,n+1,i): # we mark all multiples of 2 like this 2*2,3*2,4*2..10*2 = 20 then stops
            # this loop is main loop which finds and marks all the non prime numbers.
            prime[j] = False
p=[]
for i in range(2,n+1):
    if prime[i]:
        p.append(i)
print(p,end=" ")
print("count:",len(p))