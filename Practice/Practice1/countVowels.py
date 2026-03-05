string="pythOn".lower()
count=0
for i in string:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        count+=1
print(count)

# 2
str1="tharun kumar"
vowels="aeiouAEIOU"
c=0
for i in str1:
    if i in vowels:
        c+=1
print(c)

# 3
text="comprehension"
vowels="aeiouAEIOU"
count=sum(1 for ch in text if ch in vowels)
print(count)

# 4 using count method
str2="javafullstack".lower()
ct=str2.count('a')+str2.count('e')+str2.count('i')+str2.count('o')+str2.count('u')
print(ct)

# 5 using list comprehension
str3="pythondeveloper"
vow="aeiouAEIOU"
co=len([i for i in str3 if i in vow]) # it stores all the vowels in list first and then next find that list length.
print(co)
