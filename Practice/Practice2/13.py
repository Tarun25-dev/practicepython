# Find the first character in a string that does not repeat.
# Example: 'aabbcde' → c | 'aabb' → -1 (no unique char)

from collections import Counter
s = input("Enter string:")
freq = Counter(s)
result = next((c for c in s if freq[c] == 1), -1)
print(result)