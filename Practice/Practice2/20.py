# Compress a string using run-length encoding. If compressed is longer, return original.
# Example: 'aaabbbcc' → 'a3b3c2' | 'abc' → 'abc'

s = input()
compressed = ''
i = 0 
while i < len(s):
    count = 1
    while i+count < len(s) and s[i+count] == s[i]: count+=1
    compressed += s[i] + (str(count) if count > 1 else '')
    i+=count
print(compressed if len(compressed) < len(s) else s)