# Convert decimal to binary and binary to decimal.
# Example: 10 → 1010 | 1010 → 10

n = int(input("Enter decimal:"))
# decimal to binary
print(bin(n)[2:]) # why we use slicing with from 2 beacuse the result of bin(n) is contains strating two didgits with 0b but we dont want that we need exact binary so we slice that.
# 0 indicates a number literal(a fixed value writtern directly in the code)
# b indicates binary (base 2)

# binary to decimal
b = input("Enter binary:")

print(int(b,2)) # int(string, base)
# int(a,2) is a py function used to convert a binary number(base-2) into a decimal number(base-10).
# string : the number written as a string
# base : the number system of that string 