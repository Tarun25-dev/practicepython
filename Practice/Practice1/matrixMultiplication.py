# row x column rule - Multiply elements of a row from a matrix A with elements of a column from Matrix B
# rules : you can multiply elements of a row from matrix A with elements of a column from Matrix B then add them
# example:
# A = 2x3
# B = 3x4
# result matrix = 2x4

m1=[[10,20,30],[30,40,50],[70,30,60]]
m2=[[30,10,20],[50,10,20],[60,30,20]]
r=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(m1)): # for rows of m1
    for j in range(len(m2[0])): # for columns of m2
        for k in range(len(m2)): # for rows of m1
            r[i][j] += m1[i][k]*m2[k][j] # remember this line enough with three loops
print(r)
