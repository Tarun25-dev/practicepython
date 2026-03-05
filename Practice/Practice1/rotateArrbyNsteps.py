li=[10,20,30,40,50,60,70,80,90]
k=int(input("Enter K value:"))
print(li)
n=len(li)
k=k%n
l=0
r=n-1

while l < r: # this loop reverse total array
    li[l],li[r]=li[r],li[l]
    l+=1
    r-=1
    
l=0
r=k-1
while l < r: # this loop reverse the starting k elements
    li[l],li[r]=li[r],li[l]
    l+=1
    r-=1
    
l=k
r=n-1
while l < r: # this loop makes remaining array reverse
    li[l],li[r]=li[r],li[l]
    l+=1
    r-=1
print(li)

# 2 using slicing
li1=[10,20,30,40,50,60,70,80,90]
step=3
li1=li1[-step:]+li1[:-step]
print(li1)

    
