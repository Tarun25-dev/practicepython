import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr[1:4]) #[2,3,4]
print(arr[:5]) #[1,2,3,4,5]
print(arr[0:5:2]) #[1,3,5]
print(arr[1:4:-1]) #[] # beacuse if we go from backward using -1 then definitly start value biggerthan stop value otherwise it returns empty array
print(arr[::-1]) #[6,5,4,3,2,1]