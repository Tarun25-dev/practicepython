# Given an array, print the frequency of each unique element in order of first appearance.
li=[1,2,2,3,1,4]
k = {}
for i in li:
    if i not in k:
        k[i]=1
    else:
        k[i]+=1
for k,v in k.items():
    print(k,"-->",v)
