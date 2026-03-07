# Rotate array to the left by K positions.
# Example: arr=[1,2,3,4,5], K=2  →  Output: [3,4,5,1,2]

arr=[1,2,3,4,5]
n = len(arr)
k=int(input("Enter K value: "))
k = k % n
# why we need to take the reminder of k witth n beacuse
# in case if the k value is more than the array elements it should be rerotate and calculate the pos where last is exists.
# Suppose K = 7 then k = 7 % 5, k = 2
# rotating 7 times is same as rotating 2 times.
# So % n reduces extra rotations.
result = arr[k:] + arr[:k]
print(result)