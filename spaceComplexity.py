"""
Space complexity - Space Complexity is the amount of extra memory an algorithm uses as input size grows.
(or)
Space complexity defines how much extra memory that the code uses.

Notations:

O(1) - Uses fixed memory 
Ex: only variables,iterative binary search

O(n) - Memory grows with input 
Ex: arr=[19,30,50,60,70,8,54,3,3,2] # this is input size n
    new=[]
        for i in arr:
        new.append(i)

O(n^2) or Quadratic space complexity - very high memory uses
Ex: 2d array (nxn space)
matrix=[[0]*n for _ in range(n)] # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

O(log n) - Very small memory growth
Ex: Recursion(Binary search)
each function call uses memory in the call stack 
like,
first call - size n
second call - size n/2
third call - size n/4
...
...
so each call takes a little memory
 
if array size 16 
calls go like : 16>8>4>2>1 
total= 5 calls
16%2=8
8%2=4
4%2=2
2%1=1
if we reach 1 then stop it 
and if len of n is 16 then log2(16)=4

"""
