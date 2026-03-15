# Given first term a, ratio r, and terms n, find the GP(Geometric progression) sum.
# Formula: Sum = a * (r^n - 1) / (r - 1)  when r != 1

a = int(input())
r = int(input())
n = int(input())

if r == 1:
    print(a * n)
else:
    print(a*(r**n - 1)/(r-1))