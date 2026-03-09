# Find the contiguous subarray with the maximum sum.
# Example: Input: [-2,1,-3,4,-1,2,1,-5,4]  →  Output: 6 (subarray: [4,-1,2,1])

arr = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = cur_sum = arr[0]
for x in arr[1:]: # here we already taken default value for maximum and current sum as first element arr[0] so we can start from index 1.
    cur_sum = max(x,cur_sum+x)
    max_sum = max(max_sum,cur_sum)
print(max_sum)
