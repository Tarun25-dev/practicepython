# Print first N terms of Fibonacci series.
# Example: N=7 → 0 1 1 2 3 5 8

n = int(input())
a,b = 0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
    