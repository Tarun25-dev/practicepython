li=[1,2,3,4,1,1,1,4,4,7,9,4,3,2]
r={}
for i in li:
    if i not in r:
        r[i]=1
    else:
        r[i]+=1
for k,v in r.items():
    print(k,"-->",v)

# 2
li1=[20,20,10,10,30,40,50,30]
for i in set(li1):
    print(i,"-->",li1.count(i))

# 3
from collections import Counter
li2=[1,2,3,4,1,2,3,7,8,5]
print(Counter(li2)) #this counts all at a time and returns an object type data.

# 4
li3=[2,1,3,5,2,7,3,5,8,1,4,3]
visited=[]
for i in li3:
    if i not in visited:
        ct=0
        for j in li3:
            if i == j:
                ct+=1
        print(i,"-->",ct)
        visited.append(i)
