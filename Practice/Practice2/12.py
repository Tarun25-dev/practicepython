# two strings, check if they are anagrams of each other.
# Example: 'listen' and 'silent' → YES | 'hello' and 'world' → NO

s1 = str(input("Enter s1:")).lower()
s2 = str(input("Enter s2:")).lower()
print("Yes, Anagram" if sorted(s1) == sorted(s2) else "No, Not an Anagram")