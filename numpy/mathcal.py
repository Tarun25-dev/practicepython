# math operations on array using built in methods in numpy
# math operations are fast, vectorized(a powerful process where huge chunks of data need to be processed efficiently), and element-wise by default.
# basic arthimetic
import numpy as np
a=np.array([1,2,3,4])
b=np.array([9,8,7,6])
print(a+b) # [10 10 10 10]
print(a-b) # [-8 -6 -4 -2]
print(a*b) # [ 9 16 21 24]
print(a/b) # [0.11111111 0.25       0.42857143 0.66666667]
print(a//b) # [0 0 0 0]
print(a%b) # [1 2 3 4]
print(a**b) # [   1  256 2187 4096]

#scalar operations
print(a+2) # [3 4 5 6]
print(a*4) # [ 4  8 12 16]
print(b/2) # [4.5 4.  3.5 3. ]

# common math functions
# abs means absolute value it returns if any negative num is there then it removes that sign and prints
c=np.array([-1,-2,-3,-9,-8,-7])
print(np.abs(c)) # [1 2 3 9 8 7]
print(np.sqrt(b)) # [3.         2.82842712 2.64575131 2.44948974] it reurns in floating type
print(np.square(a))
d=np.array([1.2,5.5,5.8,6.2,9.8,1.0])
print(np.round(d)) # [ 1.  6.  6.  6. 10.  1.] if decimal less than .5  then it takes down value otherwise it takes up value.

# aggregation math
print(np.sum(a)) #10
print(np.mean(a)) #2.5
print(np.median(b)) #7.5
print(np.max(a)) #4
print(np.min(b)) #6

# for 2d arrays we use axis if it is o it goes row wise else it goes column wise
e=np.array([[1,2,3],
            [4,5,6],
            [6,7,8]])
print(np.sum(e,axis=0)) #[11 14 17]
print(np.sum(e,axis=1)) #[ 6 15 21]

# comparision math
# used in filtering
f=np.array([10,20,30,40,50,60,70,80,90])
print(f>20) #[False False  True  True  True  True  True  True  True]
# if you want values instead of true or false
print(f[f>10]) # [20 30 40 50 60 70 80 90]

# matrix multiplication use @ symbol when matrix has n*n matrix
g=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
h=np.array([[9,8,4],
            [4,3,2],
            [5,4,3]])
print(g @ h)

"""[[ 32  26  17]
    [ 86  71  44]
    [140 116  71]]"""

#shape rule if a matrix has mxn and b matrix has nxp then if we perform matrix it gives in mxp shape
