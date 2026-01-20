li=[10,20,30,40,50,60,50]
d={}
for i in li:
    d[i]=d.get(i,0)+1
for k,v in d.items():
    if v>=2:
        print(k)

# 2
li1=[10,20,30,40,50,60,50]
dic={}
for i in li1:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for k,v in dic.items():
    if v >= 2:
        print(k)

# 3
li2=[10,20,30,40,50,60,50,60,30]
li3=[]
for i in range(len(li2)-1):
    for j in range(i+1,len(li2)):
        if li2[i]==li2[j]:
            li3.append(li2[i])
print(li3)
print(set(li3)) # this works for when multiple duplicates are there

# 4
li4=[10,20,30,40,50,60,50,60,30]
li5=[]
for i in li4:
    if li4.count(i)>=2:
        li5.append(i)
print(set(li5))