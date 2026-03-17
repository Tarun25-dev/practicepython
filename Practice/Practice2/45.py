# Binary search
# Problem: Search for element X in sorted array.
# Return index (1-based) or -1 if not found.

n = int(input())
arr = [int(input()) for _ in range(n)]
x = int(input()) # target element
low,high = 0,n-1
result = -1

while low <= high:
    mid = (low+high) // 2
    if arr[mid] == x:
        result = mid+1
        break
    elif arr[mid] < x:
        low = mid+1
    else:
        high = mid-1   
print(result)