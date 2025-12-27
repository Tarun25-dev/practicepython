"""Intersection of Two Arrays
Return intersection of two arrays.
"""
li1=[1,2,3,4,7,8,9]
li2=[5,6]
result=[]
ipos=int(input("Enter index value:"))
if ipos < 0 or ipos > len(li1):
    print("index not valid")
    exit()
for i in range(len(li1)):
    if i==ipos:
        for j in range(len(li2)):
            result.append(li2[j])
    result.append(li1[i])
print(result)

# method 2
output=li1[:ipos]+li2+li1[ipos:]
print(output)