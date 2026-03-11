# Find the longest word in a given sentence. If tie, print the first one.
# Example: 'I love programming' → programming

s = input("Enter sentense:").split()
print(max(s,key=len))
