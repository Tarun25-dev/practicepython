"""Contains Duplicate
Return true if any value appears at least twice.
"""
li=[10,20,30,40,20,50,80,66,55,4,3,2,22]
is_atleast2dup=False
count=0
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]==li[j]:
            is_atleast2dup=True
            break
print(is_atleast2dup)

# method 2
print(len(li)!=len(set(li))) # if there is difference after convert into set then definetly there are duplicates

# method 3
dic={}
for i in li:
    dic[i]=dic.get(i,0)+1
is_moredups=False
for i in dic.values():
    if i >=2:
        is_moredups=True
        break
print(is_moredups)

# method 4

is_dup=False
for i in li:
    if li.count(i)>=2:
        is_dup=True
        break
print(is_dup)
    