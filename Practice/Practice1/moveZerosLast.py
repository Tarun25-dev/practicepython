# 1 using two loops
li=[1,2,3,4,10,0,3,1,0,1,0,0,5,6,0]
count=li.count(0)
j=0
for i in li:
    if i != 0:
        li[j]=i
        j+=1
for i in range(len(li)-1,len(li)-count-1,-1):
    li[i]=0
print(li)

# 2 using two pointers with one loop
li1=[1,2,3,4,10,0,3,1,0,1,0,0,5,6,0]
j=0 # which goes every index and points that location for replace with i when that j is zero
for i in range(len(li1)): # i goes every element but if statement executes when the element has not a zero
    if li1[i] != 0:
        li1[i],li1[j]=li1[j],li1[i]
        j+=1
print(li1)

# 3
li2=[1,2,3,4,10,0,3,1,0,1,0,0,5,6,0]
c=li2.count(0)
li2=[i for i in li2 if i != 0]+[0]*c # the about list will be in garbage collection so currently this li will be in a memory
# we get first this list [1, 2, 3, 4, 10, 3, 1, 1, 5, 6] after that it will fill with zero upto zeros count
print(li2)
