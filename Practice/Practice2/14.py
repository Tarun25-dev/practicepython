# Reverse the order of words in a sentence (not individual characters).
# Example: 'Hello World TCS' → 'TCS World Hello'

s = input("Enter string:")
print(" ".join(s.split()[::-1]))
