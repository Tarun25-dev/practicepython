# Find GCD (Greatest Common Divisor) and LCM of two numbers.
# Example: 12, 18 → GCD: 6, LCM: 36

from math import gcd
a,b=int(input()),int(input())
g = gcd(a,b)
print("GCD:",g)
print("LCM:",a*b//g)