# Given first term a, common difference d, and number of terms n, find the sum of AP(arthmetic progression).
# Formula: Sum = n/2 * (2a + (n-1)*d)

a = int(input())
d = int(input())
n = int(input())
sum = n*(2*a + (n-1)*d)//2
print(sum)