"""Plus One
Given digits representing a number, add one.
[1,2,3,4] --> [1,2,3,5] add last one 
[1,2,3,9] --> [1,2,4,0] add carry for next item from last
[1,2,9,9] --> [1,3,0,0] carrys moves up to a number that doesnt exists carry
[9,9,9,9] --> [1,0,0,0] if at last of the list carry exists then place a new element at last with carry 1
the process moves from last to first
"""
li=[1,2,9,9]
for i in li:
    if i > 9 or i < 0:
        print("Items in list are not valid")
        exit()
for i in range(len(li)-1,-1,-1):
    if li[i]<9:
        li[i]+=1
        break
    else:
        li[i]=0
if li[0]==0:
    li=[1]+li
print(li)
