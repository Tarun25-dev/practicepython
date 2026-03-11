# Determine if a string has all unique characters (case-sensitive).
# Example: 'abcde' → YES | 'abcda' → NO

s = input()
print("YES" if len(s) == len(set(s)) else "NO")