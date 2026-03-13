# Find sum of digits of N. Keep summing until single digit (digital root).
# Example: 9875 → 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2 (Digital Root: 2)
# digital root means repeatedly adding digits of a number until a single digit number.

n = int(input("Enter a number:"))

# using formula modulus with 9
if n%9 ==0 and n!=0:# if a number is multiple of 9 the digital root should be 9 not 0
    dr = 9
else:
    dr = n%9
print(dr)

# 2 
while n >=10:
    s = 0
    while n > 0:
        s = s+n%10 # here we adding last number to sum
        n = n//10 # here we remove that adding number from n
    n = s 
print(n)
