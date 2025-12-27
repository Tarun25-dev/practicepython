"""Pangram Check
Return true if sentence contains all letters a–z at least once.
"""
sentense=str(input("Enter sentense:")).lower()
word=""
for i in sentense:
    if i.isalpha():
        word=word+i
result={}
for ch in word:
    result[ch]=result.get(ch,0)+1
if len(result)==26:
    print("isPangram")
else:
    print("notPangram")
 
#method 2

sen=input("Enter sentense:").lower()
sent=""
for i in sen:
    if i.isalpha():
        sent+=i
a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=v=w=x=y=z=False
for ch in sent:
    if ch=="a":a=True
    if ch=="b":b=True
    if ch=="c":c=True
    if ch=="d":d=True
    if ch=="e":e=True
    if ch=="f":f=True
    if ch=="g":g=True
    if ch=="h":h=True
    if ch=="i":i=True
    if ch=="j":j=True
    if ch=="k":k=True
    if ch=="l":l=True
    if ch=="m":m=True
    if ch=="n":n=True
    if ch=="o":o=True
    if ch=="p":p=True
    if ch=="q":q=True
    if ch=="r":r=True
    if ch=="s":s=True
    if ch=="t":t=True
    if ch=="u":u=True
    if ch=="v":v=True
    if ch=="w":w=True
    if ch=="x":x=True
    if ch=="y":y=True
    if ch=="z":z=True
if a and b and c and d and e and f and g and h and i and j and k and l and m and n and o and p and q and r and s and t and u and v and w and x and y and z:
    print("is Pangarm")
else:
    print("not a pangram")

# method 3

sentence=input("Enter senetence:").lower()
li=[0]*26
for ch in sentence:
    if "a"<=ch<="z":
        index=ord(ch)-ord("a")
        li[index]+=1 # counts
is_pangram=True
for i in li:
    if i==0:
        is_pangram=False
        break
if is_pangram:
    print("pangram")
else:
    print("not pangram")
 