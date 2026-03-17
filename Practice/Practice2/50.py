# Problem: Given an N×M matrix and a target,
# find whether target exists. 
# Print (row, col) or 'Not Found'.

n,m = int(input()),int(input())
matrix = [[int(input()) for _ in range(m)] for _ in range(n)]
target = int(input("Enter target"))
found = False
for i in range(n):
    for j in range(m):
        if matrix[i][j] == target:
            print(f"found at row:{i+1}, col:{j+1}")
            found = True
            break 
    if found:
        break
if not found:
    print("Not found")