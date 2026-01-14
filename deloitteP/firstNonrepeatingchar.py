s="aabbcdd"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for k,v in d.items():
    if v==1:
        print(k)
        break

# 2
st="aabbccddefggh"
f={}
for i in st:
    f[i]=f.get(i,0)+1 # get() is a safe way to access a value from a dictionary. syntax: dictionary.get(key,default_value) if key exists in dict then it shows its value if key doesnt appear it shows default value which is useful when we are facing keyvalue error 
for i in st:
    if f[i]==1:
        print(i)
        break

# 3
string="ttrfdfs"
for i in string:
    count=0
    for j in string:
        if i==j:
            count+=1
    if count==1:
        print(i)
        break

# 4 
text="aapple"
for i in text:
    if text.count(i) == 1:
        print(i)
        break
