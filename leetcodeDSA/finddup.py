""" Remove Duplicates (Sorted Array)
Remove duplicates in-place and return new length.
"""
li=[10,1,23,11,32,87,55,14,13,10,5,5,64]
for i in range(len(li)-1):
    for j in range(len(li)-1-i):
        if li[j]>li[j+1]:
            temp=li[j]
            li[j]=li[j+1]
            li[j+1]=temp
# [1, 5, 5, 10, 10, 11, 13, 14, 23, 32, 55, 64, 87]
i=0
while i<len(li)-1:
        if li[i]==li[i+1]:
            del li[i+1]
        else:
            i+=1  
print(li)

# method 2
li2=[10,1,23,11,32,87,55,14,13,10,5,5,64]
li2.sort(reverse=False)
i=0
while i<len(li2)-1:
    if li2[i]==li2[i+1]:
        li2.pop(i+1)
    else:
        i+=1
print(li2)