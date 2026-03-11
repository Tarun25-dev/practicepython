# Count how many times a pattern appears in the main string (overlapping not counted).
# Example: Main='aababab', Pattern='ab' → 3

main = input()
pattern = input()
print(main.count(pattern))