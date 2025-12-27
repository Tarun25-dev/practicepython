"""Rotate Array
Rotate array to the right by k steps.
li[1,2,3,4,5]
k=3 last  three elements place at right of list
result=[3,4,5,1,2]
"""
li=[10,20,30,40,50,60,70,80,90]
k=int(input("Enter k value:"))
k=k%len(li)
if k < 0 or k > len(li):
    print("k more than list items / incorrect k value")
    exit()
i,j=0,len(li)-1
while i<j:
    li[i],li[j]=li[j],li[i]
    i+=1
    j-=1
i,j=0,k-1
while i<j:
    li[i],li[j]=li[j],li[i]
    i+=1
    j-=1
i,j=k,len(li)-1
while i<j:
    li[i],li[j]=li[j],li[i]
    i+=1
    j-=1
print(li)


