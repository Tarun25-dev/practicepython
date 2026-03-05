p="{[()]}"
s=[]
d={'}':'{',']':'[',')':'('} # we want to use for compare if the value matches with stack if matches returns its another pair
is_valid=True
for i in p:
    if i == '(' or i == '[' or i == '{': # or we write if i in '{([':
        s.append(i)
    else: # checking for its closed bracket
        if not s or s[-1] != d[i]:
            is_valid=False
            break
        s.pop() # this works when pair matches and also if statement fails only
if len(s)==0 and is_valid:
    print("valid brackets")
else:
    print("not a valid brackets")
    
