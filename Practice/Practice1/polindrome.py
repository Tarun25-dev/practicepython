name="madam"
left=0
right=len(name)-1
is_polindrome=True
while left < right:
    if name[left] != name[right]:
      is_polindrome=False
    left+=1
    right-=1
if is_polindrome:
   print("polindrome")
else:
   print("not a polindrome")

# 2 using slicing
text="madam"
print("polindrome" if text[::-1]==text else "Not a polindrome")

# 3 using all method - is a built in function in python it returns True/False
# returns True if every element in an iterable is True ex: print(all([True,True,True])) output:True
# returns False if atleast one element in an iterable is False ex: print(all([True,True,False])) output:False

string="madam"
result=all(string[i] == string[-i-1] for i in range(len(string)//2)) # True/False why -i-1 beacuse -i-1 gives you exactly opposite type of left index if index is 0 then 0-1=-1 so it is last index doing until half of string
print("polindrome" if result else "Not a polindrome")

# 4 using for-else - executes only when the loop completes normally,if doesnot execute if the loop stops using break.
s="madam"
for i in range(len(s)//2):
    if s[i] != s[-i-1]:
      print("Not a polindrome")
      break
else:
   print("Polindrome")
