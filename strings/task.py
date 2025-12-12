# find vowels in a string
name="tharun"
count=0
li=[]
for n in name:
    if n in "aeiou":
        count+=1
        li.append(n)
if count==0:
    print("no vowels are found in a string")
else:
    print("no.of vowels in a given string is:",count) #no.of vowels in a given string is: 2
    print("They are:",li) #They are: ['a', 'u']