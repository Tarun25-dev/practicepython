# reverse a number and must handle neg values also
# Example: input: 12345 output: 54321, input: -584 output: -485
# using slicing in two line

n = int(input())
print(int(str(n)[::-1]) if n > 0 else -int(str(abs(n))[::-1]))

