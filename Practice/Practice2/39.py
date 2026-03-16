# Problem: 
# Given an array where each value = max jump length from that index,
# determine if you can reach the last index from index 0.
# Example: [2,3,1,1,4] → YES | [3,2,1,0,4] → NO

n = int(input())
arr = [int(input()) for _ in range(n)]
reach = 0
for i in range(n):
    if i > reach:
        print("No")
        break
    reach = max(reach, i+arr[i])
else:
    print("Yes")
        