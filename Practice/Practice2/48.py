# Problem: 
# Count pairs (i,j) where i<j and arr[i]>arr[j].
# These are called inversions.
# Example: [3,1,2] → Inversions: 2 (3>1 and 3>2)
# example 2: [2,4,1,3,5]
# check pairs (2,1),(4,1),(4,3)

n = int(input())
arr = [int(input()) for _ in range(n)]
count = 0
for i in range(n):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            count += 1
print(count)