# "Write a program to read N key-value pairs from the user and print all keys in sorted order.

n = int(input("Enter N: "))
d = {}

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

dic=dict(sorted(d.items()))
k=dic.keys()
print(*k)
