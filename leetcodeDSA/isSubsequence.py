"""
Is Subsequence
Check if string s is a subsequence of string t.

Subsequence: a → c → e
Main string: m a i n t a i n a n c e
Find first a → found at index 1
Find c after that → found at index 11
Find e after that → found at index 12
"""
subSequence=str(input("Enter subSequence:"))
mainString=str(input("Enter mainString:"))
mainIndex=0
valid=True
for ch in subSequence:
    found=False
    while mainIndex<len(mainString):
        if mainString[mainIndex]==ch:
            found=True
            mainIndex+=1
            break
        else:
            mainIndex+=1
    if not found:
        valid=False
        break
if valid:
    print("sunsequence True")
else:
    print("subsquence Failed")


# method 2
subseq = "mnt"
main_str = "mountain"
j=0 # pointer
for ch in main_str:
    if j<len(subseq) and ch==subseq[j]:
        j+=1
if j==len(subseq):
    print("subsequnece")
else:
    print("not subsequence")
        

