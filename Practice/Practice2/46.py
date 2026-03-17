# Problem:
# Sort all words in a sentence alphabetically (case-insensitive).
# Example: 'banana apple cherry' → 'apple banana cherry'

s = input().split()
print(' '.join(sorted(s,key=lambda x:x.lower())))