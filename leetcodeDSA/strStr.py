""" Implement strStr()
Return the index of the first occurrence of needle in haystack, else -1.
"""
def function(heystack,needle):
    n=len(heystack)
    m=len(needle)
    if needle=="":
        return 0
    
    for i in range(n-m+1):
        match=True
        for j in range(m):
            if heystack[i+j] != needle[j]:
                match=False
                break
        if match:
            return i
    return -1
print(function("saytosay","say"))

# method 2
heystack="hellomyhello"
needle="hello"
print(heystack.find(needle))

# method 3
m=len(needle)
for i in range(len(heystack)-m+1):
    if heystack[i:i+m] == needle: # i+m calculates the needle len (slicing)
        print(i)
print("-1")
    



