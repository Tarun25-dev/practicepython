"""String to Integer (atoi)
Convert a string to a 32-bit integer following rules (ignore spaces, signs).
"""
s=str(input("Enter string:"))
i=0
n=len(s)
while i<n and (s[i]==" "): # remove starting any  spaces and we place i sign
    i+=1
sign=1
if i<n and (s[i]=="+" or s[i]=="-"):
    if s[i]=="-":
        sign=-1
    i+=1
num=0
while i<n and s[i].isdigit():
    num=num*10+int(s[i]) #convert to int through loop one by one charecter and store that in num variable
    i+=1
num=num*sign # actual sign assigning 

# setting range of 32 bit if input is not in this range then if statemnt executed

if num < -2**31: # min 32 int range
    num=-2**31
if num > 2**3111: # max 32-bit range
    num=2**31-1
print(num)


# method 2
string="1234srec"
i=0
while i<len(string) and string[i]==" ":
    i+=1
sign=1
if i<len(string) and string[i]=="-":
    sign=-1
    i+=1
elif i<len(string) and string[i]=="+":
    i+=1
result=""
while i<len(string) and string[i].isnumeric():
        result=result+string[i]
        i+=1
result=sign*int(result)

if result < -2**31: # min 32 int range
    result=-2**31
if result > 2**3111: # max 32-bit range
    result=2**31-1
print(result)