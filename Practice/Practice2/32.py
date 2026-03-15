# Print a hollow rectangle of * with R rows and C columns.
# Example R=4, C=6: First and last row full stars. Middle rows: * followed by spaces, then *.

r,c=int(input()),int(input())
for i in range(r):
    if i == 0 or i == r-1:
        print('*' * c)
    else:
        print('*'+' '*(c-2)+'*')