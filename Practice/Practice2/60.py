# You are given an array of weights: arr[]
# You are given a maximum allowed weight: X
# You need to find how many people can be selected such that their total weight ≤ X

arr = [100,234,178,375,979,555,342]
x = int(input("Enter x value:"))
for i in range(len(arr)):
    for j in range(0,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

count = 0
sum = 0
for i in arr:
    if sum+i <= x:
        sum += i
        count += 1
    else:
        break
print(count)


   
