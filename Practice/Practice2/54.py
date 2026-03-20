num=int(input())
result=""
while num > 0:
  result = str(num%2)+result
  num = num//2
print(result)
