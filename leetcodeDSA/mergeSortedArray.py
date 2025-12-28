"""Merge Sorted Array
Merge two sorted arrays into one sorted array.
"""
li1=[1,6,4,2,6,7,8]
n=len(li1)
li1.sort()
li2=[5,6,7,2]
li2.sort()
li1.extend([0]*len(li2))
j=0
for i in range(n,len(li1)):
    li1[i]=li2[j]
    j+=1
for i in range(len(li1)):
    for j in range(len(li1)-1-i): # reason for that len(li1)-1-i means len(li1)-1 makes the last index which means len is 3 then last index is 2 beacuse we already taken that in loop as j+1. why we substract i means at every itereation it sets the larger number at last so  we dont need to check again in j loop so we also remove that. 
        if li1[j]>li1[j+1]:
            li1[j],li1[j+1]=li1[j+1],li1[j]
print(li1)