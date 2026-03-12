# A number is Armstrong if sum of its digits each raised to power(number of digits) equals the number. 153 = 1³+5³+3³ = 153.

n = int(input())
power = len(str(n))
num = n
result=0
while num!=0:
    d = num % 10
    result+=d**power
    num=num//10
print("armstrong" if result == n else "Not armstrong")