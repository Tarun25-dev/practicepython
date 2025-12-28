"""Majority Element
Find element appearing more than n/2 times.
"""
li=[1,2,3,2,2,1,2,2,5,2,1,1,1,1,1,1,1,1]
count=len(li)//2
dic={}
for i in li:
    dic[i]=dic.get(i,0)+1
for k,v in dic.items():
    if v>count:
        print(k)

# method 2
ct=len(li)//2
mcount=0
melement=0
for i in range(len(li)):
    temp=1
    for j in range(i+1,len(li)):
        if li[i]==li[j]:
            temp+=1
    if temp>mcount and temp>ct:
        mcount=temp
        melement=li[i]
print("Number:",melement,"count:",mcount)

