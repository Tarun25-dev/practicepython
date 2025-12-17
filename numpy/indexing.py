import numpy as np
array=np.array([1,2,3,4,5])
array[0]=0 # updates beacuse arrays are mutable but can't adjust size auto, not like list.
arr=np.insert(array,3,6) # if we use insert size auto increase one at a time.
print(array) # [0 2 3 4 5]
print(arr) # [0 2 3 6 4 5]
print(arr[0]) #0
print(arr[-1]) #5
print(arr[2]) #3