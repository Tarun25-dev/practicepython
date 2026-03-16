# Problem: 
# A factory has chocolate packets. Empty packets (0) must be moved to end of conveyor belt.
# Input: N, then N integers (array). 0 = empty packet.
N = int(input("Enter conveyor size:"))
arr = [int(input()) for _ in range(N)]
result = [x for x in arr if x!=0]+[0]*arr.count(0)
print(result)