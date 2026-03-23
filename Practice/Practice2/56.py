# reverse a number and must handle neg values also
# Example: input: 12345 output: 54321, input: -584 output: -485

num = int(input())
sign ="-" if num < 0 else ""
# first we need to convert any neg values to pos values using abs() and for sign we also stored
n = abs(num)
rev = 0

while n > 0:
    d = n % 10
    rev = rev * 10 + d
    n = n // 10

print(f"{sign}{rev}")