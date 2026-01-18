# 1 using slicing and less optimal
str1="listen"
str2="silent"
if len(str1) != len(str2):
    print("Is not an Anagram")
    exit()
for i in str1:
    if i in str2:
        index=str2.find(i)
        str2=str2[:index]+str2[index+1:]
if len(str2) == 0:
    print("Anagram")
else:
    print("Not an anagram")
    
# 2 using sorting optimal approach for better to use sorted() function
str3=list("listen") # beacuse strings are immutable
str4=list("silent")

if len(str3)!=len(str4):
    print("Not an anagram")
    exit()
for i in range(len(str3)-1):
    for j in range(len(str3)-1):
        if str3[j] > str3[j+1]:
            str3[j],str3[j+1]=str3[j+1],str3[j]
        if str4[j] > str4[j+1]:
            str4[j],str4[j+1]=str4[j+1],str4[j]
print("Anagram" if str3==str4 else "Not an anagram")

# 3 using dictionary/hashmap optimal 
str5="listen"
str6="silent"
if len(str5) != len(str6):
    print("Is not an Anagram")
    exit()
s1={}
s2={}
for i in str5:
    if i not in s1:
        s1[i]=1
    else:
        s1[i]+=1
for j in str6:
    s2[j]=s2.get(j,0)+1 
print("Anagram" if s1 == s2 else "Not an anagram")# we directky compare dicts beacuse py checks same keys has same values not order

# 4 using count()
str7="listen"
str8="silent"
is_anagram=True
if len(str7) != len(str8):
    is_anagram=False
    exit()
for i in str7:
    if str7.count(i) != str8.count(i):
        is_anagram=False
print("Anagram" if is_anagram else "Not an anagram")

# 5 using counter module
str9="listen"
str10="silent"
from collections import Counter
if Counter(str9)==Counter(str10):
    print("Anagram")
else:
    print("Not an anagram")
    