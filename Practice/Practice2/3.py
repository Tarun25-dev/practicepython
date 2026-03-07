# Find missing Number

li=[1,2,3,4,5,7,8]
n = max(li)
actualSum = n*(n+1)//2
originalSum = 0
for i in li:
    originalSum +=i
misElement = actualSum - originalSum
print(misElement)