"""Single Number
Every element appears twice except one — find it.
"""
li=[1,7,5,1,4,7,5]
dic={}
for i in li:
    dic[i]=dic.get(i,0)+1
is_found=False
for k,v in dic.items():
    if v==1:
        print(k)
        is_found=True
        break
if not is_found:
    print("There is no single element in list")
    
# same for letters also 
li1=[1,3,4,5,1,3,4]
is_single=False
sElement=0
for i in range(len(li1)):
    is_single=True
    for j in range(i+1,len(li1)):
        if li1[i]==li1[j]:
            is_single=False
    if is_single:
        sElement=li[i]
        is_single=True
if is_single:
    print(sElement)
else:
    print("No single element")
            
# using Xor
# rules if two inputs are differ then it is true else false
# x^x=0
# x^0=x or 0^x=x
# how xor works means dup numbers cancels each other and only the single number remains.
single=0
for i in li:  
    single=single^i
print(single)