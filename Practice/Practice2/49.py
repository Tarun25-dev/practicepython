# Problem:
# Sort elements by frequency (most frequent first).
# If same frequency, sort by value.
# Example: [4,4,2,2,2,3] → [2,2,2,4,4,3]
from collections import Counter
arr = [4,4,2,2,2,3]
# print(Counter(arr)) # Counter({2: 3, 4: 2, 3: 1}) this already gives me in sorted
freq = Counter(arr)
result = []
for num,count in freq.most_common():
    result.extend([num]*count) # extend adds many items than append
print(result)
    
