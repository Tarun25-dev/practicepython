# Numpy - Numerical python is a Python library used to work with numbers and arrays very fast.
# Numpy is used for:
# Used for: Fast calculations, Working with numbers, Arrays (better than Python lists), Foundation for Pandas, ML, AI.

# why numpy array over python list

# list              |   Array
#-------------------------------------------
# Slow	            |   Very fast 
# Mixed data types	|   Same data type
# Limited math	    |   Powerful math
# Manual loops	    |   Vectorized ops

# vectorized operations means:
# Operation applies to all elements together
# No manual loop
# Faster because NumPy uses C internally
# Python loop:
# You tell the worker every single step
# NumPy:
# You give one command, worker finishes everything.

# Internally:
# Python calls NumPy
# NumPy hands work to C code
# C loop runs on raw memory
# Result returned to Python
# Python loop avoided
# this checks if your system has installed nupmy or not, is installed it shows version otherwise it shows no numpy package is there
# import numpy as np
# print(np.__version__)
# install
# run "pip install numpy" on cmd or project current directory terminal

# creating my first numpy as array
import numpy as np
array=np.array([1,2,3,4,5,6,7,8,9,])
print(array) # [1 2 3 4 5 6 7 8 9]
print(len(array)) # 9
print(type(array)) # <class 'numpy.ndarray'>

# difference between list and array is 
li=[1,2,3]
print(li*2) # [1, 2, 3, 1, 2, 3] - duplicates list
arr=np.array([1,2,3])
print(arr*2) # [2 4 6] - multiply values


