li=[1,2,3,4,5,6,7,9]
actualSum=0
for i in range(len(li)):
    actualSum+=li[i]
n=li[-1]
originalSum=n*(n+1)//2 # this formula works for 0 to n sum 
missingDigit=originalSum-actualSum
print("No Missing digit" if originalSum == actualSum else missingDigit)

# if we have to check the missing element at particular range then we use formula sum= sum(1 to b) - sum(1 to a-1)
# a = the starting number of the range
# b = the ending number of the  range
# we first sum from 1 to ending point and then we remove the part from 1 to a-1 so we get a to b

li1=[4,5,6,7,9]
a,b=li1[0],li1[-1]
curSum=sum(li1)
orgiSum=(b*(b+1)//2)-(a*(a-1)//2)
print(orgiSum-curSum)
