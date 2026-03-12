# Given a number N, check if it is prime.
# Example: 7 → Prime | 12 → Not Prime

num = int(input("Enter a number:"))
n=num
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2,num):
        if num % i == 0:
            is_prime=False
print("Prime number" if is_prime else "Not a Prime number")