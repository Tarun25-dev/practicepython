# zip() is a built-in function used to pairs items from multiple iterables into a single iterator of paired elements
# it works on strings, lists, tuples,etc.
# it works well for same length if len is not same it adjuts with small size and remaining elements are not considered.
# useful when we are working with multiple loops 
# Example:
a=[22,33,23,11,43,21]
b=["a","b","c","d","e","h"]
for i,j in zip(a,b): # now we can access i from a and j from b at a time
    print(i,j)
print(list(zip(a,b))) # [(22, 'a'), (33, 'b'), (23, 'c'), (11, 'd'), (43, 'e'), (21, 'h')]

# converting two lists into dict with efficient way
c=[22,33,23,11,43,21]
d=["a","b","c","d","e","h"]
dic=dict(zip(c,d)) # without any loops are used we converted two lists into one dictionary
print(dic)

# we can also take multiple lists,string,tuples
e=[22,33,23,11,43,21]
f=["a","b","c",76,"e","h"]
g=[12,33,"e",44,85,"kk"]
for i,j,k in zip(e,f,g):
    print(i,j,k)