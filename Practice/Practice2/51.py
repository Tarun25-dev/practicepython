# problem: sweet seventeen(base conversion):
# you are given a number in base 17(figits go from 0 to 9 and A(10) to G(16))
# convert this number into its decimal(base 10) equivalent.
# simple formula: result = result * base + digit
# noraml cal: ex: 23GF(231615) = 2*17**3 + 2*17**2 + 16*17**1 +15*17**0 = (10980)base 10
 
def convert(ss,base):
    result = 0
    for i in ss:
        if i.isdigit():
            value = int(i)
        elif i.isalpha():
            value = ord(i.upper()) - ord('A') + 10
        else:
            print("worng Input")
        result = result * base + value 
    return result

ss = input("Enter base 17 value:")
base = 17
print(convert(ss,base))

        