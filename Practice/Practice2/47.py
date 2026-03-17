# Problem: 
# Find the Kth largest element in an unsorted array without full sorting.
# Example: arr=[3,2,1,5,6,4], K=2 → Answer: 5

n = int(input())
arr = [int(input()) for _ in range(n)]
k = int(input("Enter k:"))
arr.sort(reverse=True) # largest to smallest
print(arr[k-1])
