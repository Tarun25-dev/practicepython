li=[10,20,30,40,33,23,10,5]
low=0
high=len(li)-1
while low<high:
    mid=(low+high)//2
    if li[mid]<li[mid+1]:
        low=mid+1
    else:
        high=mid
print(low) # index
print(li[low]) # value
