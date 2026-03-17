# Problem: 
# Sort array using Bubble Sort. 
# Print array after each pass or just final sorted array

n = int(input())
arr = [int(input()) for _ in range(n)]
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)