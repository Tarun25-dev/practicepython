# A set is a collection of unique items. -Unordered, No duplicates allowed, Mutable, Uses {} or set() to create
# why the sets be follows unordered
# beacuse 
# Python sets use a hash table internally to store elements.
# A hash table stores data based on a hash value (a special number computed from the element).
# Position in memory depends on hash value, not the order you insert.
# Because elements are stored by hash values, there is no index or order.
# You cannot access s[0] like a list.

s={12,22,35,74,50}
print(s,type(s)) #<class 'set'>

# or

st=set([12,22,35,74,50])
print(st,type(st)) #<class 'set'>

# Accessing elements in set
set={10,20,30,40}
for s in set:
    print(s)

# Why Use Sets?
# To store unique items
# To do mathematical set operations (union, intersection, etc.)
# To check membership quickly (in operator)