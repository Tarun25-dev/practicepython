import numpy as np
arr1=np.array([1,2,3,4,5])
arr2=np.array([60,70,80,90,100])
arr3=np.array([[1,2,4], # o index
               [3,4,3], # 1 index
               [5,6,2], # 2 index
               [7,8,1]]) # 3 index 
arr4=np.array([[1,2,3,4,5],
               [9,8,7,6,5]])
arr5=np.array([[5,6,7,8,9],
               [5,4,3,2,1]])

# append() - adds value at last  - we cant use dirctly on main array beacuse numpy array doent have append method
arr11=np.append(arr1,6)
print(arr11)

# delete()
arr22=np.delete(arr2,3)
print(arr22) # [ 60  70  80 100]
# delete multiple elements
arr222=np.delete(arr2,[0,2,3])
print(arr222) #[ 70 100]

# axis tells the direction of operation
# row index value use if we want to delete row 
# column index value use if we want to delete column
# if axis = 0 --> rows(vertical direction)
# if axis = 1 --> columns(horizontal direction)
# deleting a row
arr33=np.delete(arr3,1,axis=0)
print(arr33)
arr333=np.delete(arr3,0,axis=1)
print(arr333)

# concatinate two arrays using np.concatenate((arr1,arr2),axis=0/1)
# axis 0 refers to join by rows
# axis 1 refers to join by columns 
arr45=np.concat((arr4,arr5),axis=0)
print(arr45)
arr54=np.concat((arr4,arr5),axis=1)
print(arr54)

# vstack(vertical stack) - vstack in NumPy is used to stack arrays vertically (row-wise) — one array on top of another.
# Arrays must have the same number of columns
import numpy as np
array1=np.array([1,2,3,4])
array2=np.array([5,6,7,8]) 
print(np.vstack((array1,array2)))
# output : first is placed top of second array
# is converted to 2d array
#[[1 2 3 4]
 #[5 6 7 8]]

# for 2d arrays
array3=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
array4=np.array([[9,8,7],
                 [6,5,4],
                 [3,2,1]])
print(np.vstack((array3,array4)))
# [[1 2 3]
# [4 5 6]
# [7 8 9]
# [9 8 7]
# [6 5 4]
# [3 2 1]]

# hstack(horizontal stack) - hstack in NumPy is used to stack arrays horizontally (column-wise) — one array on side by another.
# Arrays must have the same number of columns.

import numpy as np
array3=np.array([1,2,3,4])
array4=np.array([5,6,7,8]) 
print(np.hstack((array3,array4))) # [1 2 3 4 5 6 7 8]

# for 2d arrays
array5=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
array6=np.array([[9,8,7],
                 [6,5,4],
                 [3,2,1]])
print(np.hstack((array5,array6)))

# output:
# [[1 2 3 9 8 7]
# [4 5 6 6 5 4]
# [7 8 9 3 2 1]]

# reshape() and resize() is not numpy methods, it is an arrays methods in numpy.
# reshape(rows, columns) - The reshape() method is used to change the shape of an array without changing its data.
# 1d to 2d
ary1=np.array([1,2,3,4,5,6])
ary11=ary1.reshape(3,2)
print(ary11) 
# [[1 2]
# [3 4]
# [5 6]]

# 2d to 1d
ary2=np.array([[1,2,2],[1,4,5],[9,5,6],[9,5,2]])
ary22=ary2.reshape(12)
print(ary22) # [1 2 2 1 4 5 9 5 6 9 5 2]

# -1 tells NumPy: “You calculate this dimension for me”
ary3=np.array([1,2,3,4,5,6,7,8])
ary33=ary3.reshape(2,-1)
print(ary33)
# [[1 2 3 4]
# [5 6 7 8]]

# not going this concept deep which mainly this method related to memory ownership
# The resize() method is used to change the shape AND size of an array.
# Unlike reshape(), it modifies the original array.
# is we want to create a specific nxn shape even though we dont have that much of elements but this resize methods fills the missing values with zeros
# Extra spaces filled with 0

# flatten() - Converts any N-D array into a 1-D array
# Original array is safe
# No memory-sharing issues
# No resize errors
y=np.array([[1,2,3],
           [4,5,6],
           [7,8,9],
           [10,11,12]])
z=y.flatten()
print(z) # [ 1  2  3  4  5  6  7  8  9 10 11 12]

# where - np.where() is used to find positions or select values based on a condition.
# syntax - np.where(condition, value_if_true, value_if_false)
# Find indices - whenever it returns more than one index then is called as indices
c=np.array([10,20,30,40,20,30,90,100])
indices=np.where(c==20)
print(indices) # (array([1, 4]),)
# 20 is at 1st index and 4th index

# Replace values using condition
d=np.array([10,20,30,40,50,60,70,80,90,100])
ins=np.where(d>60,"pass","fail")
print(ins) # ['fail' 'fail' 'fail' 'fail' 'fail' 'fail' 'pass' 'pass' 'pass' 'pass']

# Change values in array
en=np.array([20,10,30,49,21,43,22])
print(np.where(en>20,0,en)) # If value ≥ 20 put 0, else keep original”
# [20 10  0  0  0  0  0]

# sort()
# In NumPy, sorting can be done in two ways:
# np.sort() → returns a new sorted array
# array.sort() → sorts the original array
# for 2d arrays Row-wise sort (default)
# for column wise sorting np.sort(a, axis=0) if we use dirctly on array it uses array method if we create a variable and use np.sort it returns new array
g=np.array([1,2,41,3,5,23,2,5,3])
h=np.sort(g,) # default row wise
print(h) # [ 1  2  2  3  3  5  5 23 41]
# descending order 
print(h[::-1]) # [41 23  5  5  3  3  2  2  1]

# for 2d arrays
i=np.array([[1,4,2,1],
            [46,43,77,55],
            [99,56,43,22]])
print(np.sort(i)) # row wise - 
# [[ 1  1  2  4]
# [43 46 55 77]
# [22 43 56 99]]

# np.unique() is used to find unique (non-duplicate) values in an array.
k=np.array([10,20,10,23,22,10,40,32])
l=np.unique(k)
print(l) # [10 20 22 23 32 40]
# removes duplicates and arrange in ascending order

# Unique + counts
values,counts=np.unique(k,return_counts=True)
print(counts)
print(values)

# [3 1 1 1 1 1]
# [10 20 22 23 32 40]
# here in k array only 10 repeats three types and remaining all values only once repeated

# Unique indices
value,index=np.unique(k,return_index=True)
print(index) # [0 1 4 3 7 6]
print(value) # [10 20 22 23 32 40]

# 2d array - Flattens automatically
# but must size has nxn
h=np.array([[1,2,3,4,8,7,5],[2,3,4,7,8,9,0]])
print(np.unique(h)) # [0 1 2 3 4 5 7 8 9]


# type conversion
# int to float like [1, 2, 3] to [1. 2. 3.]
# float to int like [1.2, 2.3, 3.4] to [1 2 3] - The decimal part is truncated → meaning it is simply removed
p=np.array([1,2,3,4])
q=p.astype(float) # we can also replace with string as str, boolean as bool
print(q) # [1. 2. 3. 4.]
print(q.dtype) # float64