# 1. UNION(|) - combines both sets
# 2. INTERSECTION(&) - common elements from both sets
# 3. DIFFERENCE(-) - elements in A but not in B
# 4. SYMMETRIC DIFFERENCE(^) - elements in A or B, but not in both

set1={10,20,30,40,50}
set2={30,40,50,60,70}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2) #{10,20} or {20,10} only beacuse these two only the elements that are not in set2
print(set2 - set1) 
print(set1 ^ set2) 
print(set2 ^ set1)
#above both are equal returns beacuse, it returns only unique values from both not any same elements in both sets are not considered