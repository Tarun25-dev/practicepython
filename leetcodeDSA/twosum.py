"""Two Sum
Given an array and target, return indices of two numbers that add up to target.
"""
li=[10,20,30,45,32,55,20]
target=int(input("Enter Target value:"))
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]+li[j]==target:
            print(i,j)
            break
