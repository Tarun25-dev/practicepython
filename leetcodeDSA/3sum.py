# givwn an integer array
# find all unique triplets
# conditions:
# each triplet must conatin exactly three numbers
# sum of the 3 numbers must be zero
# triplets must be unique and same numbers with different order are not allowed
# example li=[-1,0,1,2,-1,-4]
# output triplets are [[-1,-1,-2],[-1,0,1]] we found two triplets in the given list each must zero while sum of the three numbers
li=[-1,0,1,2,-1,-4]
li.sort()
n=len(li)
result=[]
for i in range(n-2): 
    # why i-2 beacuse i moves at last of the index n-1 but whenever the i value is last then there id no number to take for triplets. 
    # i = first number, i+1 = second number, i+2 = third number and the loop continues from 0 to n-2
    if i>0 and li[i]==li[i-1]: # this checks current number is same as previous number if it is then skip the remaining iteration and incereae the i value
        continue
    left=i+1
    right=n-1
    while left < right:
        total=li[i]+li[left]+li[right]
        if total == 0:
            result.append([li[i],li[left],li[right]])
            # skip duplicates
            while left < right and li[left]==li[left+1]:
                left+=1
            while left < right and li[right]==li[right-1]:
                right-=1
            left+=1
            right-=1
        elif total<0:
            left+=1
        else:
            right-=1
print(result)
