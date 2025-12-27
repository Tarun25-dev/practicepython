"""First Unique Character
Given a string, return the index of the first non-repeating character, else -1.

"""
string=str(input("Enter string:"))
for i in range(len(string)):
    count=0
    for j in range(len(string)):
        if string[i]==string[j]:
            count+=1
    if count==1:
        print(string[i])
        break
        
"""
get()- is used to retreive a value from a dict safely without causing a keyErorr and it allows us to give a default value if the key is missing.
"""
#method 2
s="tharun kumar"
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
for ch in s:
    if freq[ch]==1:
        print(ch)
        break
print(freq)
# method 3
for ch in s:
    if s.count(ch)==1:
        print(ch)
        break
