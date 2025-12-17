# properties of numpy
import numpy as np
array=np.array([1,2,3,4,5])
arr=np.array(["abc","bcd"])
print(array.ndim) # 1 refers to one dimensional array.
print(array.shape) # (5,) refers to 5 column values and no row values.
print(array.size) # 5 
print(array.dtype) # int64
print(arr.dtype) # u3 - unicode string and three refers the length of abc and bcd