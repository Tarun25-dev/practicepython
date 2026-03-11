# Caesar Cipher Encryption
# Shift each letter in the message by K positions (wraparound at z). Digits also shift by K. Special characters remain unchanged.
# Example: 'abc', K=2 → 'cde' | 'xyz', K=2 → 'zab'

msg = input("Enter message:")
k = int(input("Enter K value:")) % 26 # 26 alphabets for ignore some cases like if z is a first value then apply k shift we should go again repeat from a so which gives reminder
result = ''
for c in msg:
    if c.isalpha(): # if c value must alpha then only this condition executes.
        base = ord('a') if c.lower() else ord('A') # ord converts alpha to ascii number base value based on c variable type if it is capital then base value is 'A' = 65 else 'a' = 97
        result += chr((ord(c)-base+k)%26+base) # char converts ascii to charevter and here we take c ascii value and minus with base then we get that original ascii of that char
    elif c.isdigit():
        result += str((int(c)+k)%10) # 0 to 9 digits and we convert that char to int using int() and after adding with k we can convert to string
    else:
        result += c
print(result)
