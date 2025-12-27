"""Missing Number
Given an array containing numbers from 0 to n with one missing, find the missing number.
"""
# method1 - takes O(n)=time complexity and O(1)-space complexity
li=[0,1,2,3,4,5,7,8]
n=8
expectedSum=n*(n+1)//2 # formula for sum of numbers from 0 to n
actualSum=0
for i in li:
    actualSum+=i
if actualSum!=expectedSum:
    result=expectedSum-actualSum
    print(result)
else:
    print("no one item missing in list")

# method2
for i in range(n):
    if i not in li:
        print(i)

#method3 if not start from zero
li2=[10,15,16,17,18,19,20]
li3=[]
Max=max(li2)
Min=min(li2)
for i in range(Min,Max):
    if i not in li2:
        li3.append(i)
print(li3,"missing items in list")