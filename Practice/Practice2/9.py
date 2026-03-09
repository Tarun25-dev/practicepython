# Given a sorted array, remove duplicates and print unique elements.
# Example: Input: [1,1,2,3,3,4]  →  Output: [1,2,3,4]

arr = [1,1,2,3,3,4]
arr = set(arr)
print(list(arr))
