# Find factorial of N. Also find number of trailing zeros in N!
# Example: N=10 → 3628800, Trailing Zeros: 2
# trailing zeros means all zeros that appear end of the number

n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact*i
print("Factorial is:",fact)

# when ever we calculate trailing zeros we can use formula like temp//5+temp//25+temp//125
zeros = n//5 + n//25 + n//125 
print("No.of Trailing zeros:",zeros)