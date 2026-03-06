# Move all zeros to end in arrays
# with and without using second array

# without using second array
li=[1,4,0,2,0,2,5,6,3,0,2,0]
pos = 0
for i in range(len(li)):
    if li[i] != 0:
        li[pos],li[i] = li[i],li[pos]
        pos +=1
print(li)

# here pos is used to hold position of each value in list until its swap
# i is used for finding non-zero values to swap and if i value zero then pos doesnt update its value.

# with another list

li1=[1,4,0,2,0,2,5,6,3,0,2,0]
result = []
for i in li1:
    if i!= 0:
        result.append(i)
for i in range(len(result),len(li1)):
    result+=[0]       
print(result) 

# 2
li2=[1,4,0,2,0,2,5,6,3,0,2,0]
result = [x for x in li2 if x!=0]+[0]*li2.count(0)
print(result)