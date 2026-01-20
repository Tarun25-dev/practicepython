li=[10,40,30,22,14,9,65,44,15]
li1=[]
sum=24
for i in range(len(li)-1):
    for j in range(i+1,len(li)): # stop is excluding so it automatically -1 keeps
        print(j)
        if li[i]+li[j]==sum:
            li1.append([li[i],li[j]])
            li1.append([li[j],li[i]])
print(li1)
