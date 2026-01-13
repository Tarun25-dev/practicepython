sen="I LOVE MY COUNTRY"
longest=""
current=""
for i in sen:
    if i != " ":
        current+=i
    else:
        if len(current) > len(longest):
            longest=current
        current=""
# we know that current has last word but it cant have space to apply condition of len so we do seperately.
if len(current) > len(longest):
    longest=current
print(longest) 

# 2
s="I LOVE PYTHON LANGAUGE"
li=s.split()
high=li[0]
for i in li:
    if len(i) > len(high):
        high=i
print(high)

# 3
text="India is My country"
words=text.split()
print(max(words,key=len)) # find the max word though iterable of list and we need to give key value then only the purpose of this problem fulfilles means it finds max value based on the len
# if we dont use key then it checks the lexicographically means it checks each word though their ascii values not by len so it is important.
