"""
Time complexity - Time complexity is the measure of how the running time of an algorithm grows as the input size increases.
(or)
Time complexity is the measure of how fast code runs when input size increases.

Big-O Notation - A way to show code speed.

O(1) - An algorithm if it takes same amount of time no matter how big the input is.
Ex: arr[0],arr[1],arr[2],...

O(n) - An algorithm if it taken time increases directly with input size.
Ex: for i in arr:
       print(i)
here the loop is always runs upto last value of array and n refers to the no.of times loop executes.

O(log n) - An algarithm if it reduces the input size by half each step, so it runs very fast.
Ex: Binary search

O(n^2) or (Quadratic time complexity) - An algorithm if time grows as the square of input size.(Time increases very fast when input size increases)
Ex: for i in arr:
        for j in arr:
              print(i,j)
like,
input(n)    steps(approx.)
2           4
3           9
5           25
10          100

Easy to remember : Two nested loops over input usually mean O(n^2)
"""