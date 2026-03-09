# : Find all duplicate elements in an array (elements that appear more than once).
# Example: Input: [1,3,4,2,2,3]  →  Output: 2 3
arr = [1,3,4,2,2,3]
seen,dup = set(),set()
for i in arr:
    if i not in seen:
        seen.add(i)
    else:
        dup.add(i)
print(*sorted(dup)) # by  adding * we remove those square brackets like list to nprmal output like in the example.