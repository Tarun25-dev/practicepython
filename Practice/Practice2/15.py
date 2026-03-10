# Count total vowels and consonants in a string (ignore spaces and digits).
# Example: 'Hello World' → Vowels: 3, Consonants: 7

s = input("Enter string:")
vowels = sum(1 for c in s if c in "aeiou")
consonents = sum(1 for c in s if c not in "aeiou" and c.isalpha())
print("Vowels:",vowels)
print("Consonents:",consonents)