"""Move Zeroes
Move all zeroes to the end while maintaining order of non-zero elements.
"""
li=[0,1,0,2,0,3,0,4,0,5,6,7,8,0,9]
pos=0
for i in range(len(li)):
    if li[i]!=0:
        li[pos]=li[i]
        pos+=1
for i in range(pos,len(li)):
    li[i]=0
print(li)

# method 2
li2=[0,1,0,2,0,3,0,4,0,5,6,7,8,0,9]
pos=0
for i in range(len(li2)):
    if li2[i]!=0: # if there is zero then no need to increase the pos just increase the i value 
        li2[i],li2[pos]=li2[pos],li2[i]
        pos+=1

# method 3
li3=[0,1,0,2,0,3,0,4,0,5,6,7,8,0,9]
li4=[]
for i in li3:
    if i!=0:
        li4.append(i)
n=len(li3)-len(li4)
for _ in range(n):
    li4.append(0)
print(li4)



