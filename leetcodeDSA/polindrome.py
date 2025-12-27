# given an integer x, retuen true if it reads the same forward and backward, else false.
x=int(input("Enter an integer:"))
dup=x
temp=0
while dup>0:
    d=dup%10
    temp=temp*10+d
    dup=dup//10
if temp==x:
    print("polindrome")
else:
    print("not polindrome")


    


