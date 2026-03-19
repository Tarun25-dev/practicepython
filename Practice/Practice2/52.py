# Find the second largest element in an array without sorting.

def sec_largest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num!=first:
            second = num
    return second

n = int(input("Enter n:"))
arr = [int(input()) for _ in range(n)]
print("Second largest element is:",sec_largest(arr))