"""Valid Palindrome
Given a string, return true if it is a palindrome ignoring non-alphanumeric characters and case.
"""
def poli(n: str) ->bool: #n refers to parameter and its type str and it must returns only boolean values
    clean=""
    for ch in n:
        if ch.isalnum():
            clean+=ch.lower()
    l=0
    r=len(clean)-1
    while l<r:
        if clean[l]!=clean[r]:
            return False
        l+=1
        r-=1
    return True
print(poli("Mom"))
print(poli("s-a-s"))
print(poli("1t1"))

#method 2
def poly(s:str)->bool:
    left=0
    right=len(s)-1
    while left<right:
        if not s[left].isalnum():
            left+=1
        elif not s[right].isalnum():
            right-=1
        else:
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
    return True
print(poly("Dad"))
    




            



    