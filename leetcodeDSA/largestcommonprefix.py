"""Longest Common Prefix
Given an array of strings, return the longest common prefix.
"""
#method1
strs=["flower","flow","flight"]
prefix=strs[0]
for word in strs:
    while not word.startswith(prefix):
        prefix=prefix[:-1] # removing last letter if not
print(prefix)

#method2

n=int(input("enter list length"))
li=[]
for i in range(n):
    val=str(input())
    li.append(val)
if not li:
    print("")
else:
    r=""
for i in range(len(li[0])):
    ch=li[0][i]
    for s in li:
        if i>=len(s) or s[i]!=ch:
            print(r)
            exit()
    r+=ch
print(r)