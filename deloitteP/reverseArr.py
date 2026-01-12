# Reverse an array but we take list beacuse we are do it in python.
# list in py can be mutable,so we easily reverse in place no need to extra list for reverse.
arr=[10,20,30,40,50]
left=0
right=len(arr)-1
while left < right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
print(arr)

# using slicing
array=[10,20,30,40,50]
print(array[::-1])

# using second array
arr1=[10,20,30,40,50,60,70,80,90]
arr2=[]
for i in range(len(arr1)-1,-1,-1):
    arr2.append(arr1[i])
print(arr2)