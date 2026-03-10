# Check if a given string is a palindrome (ignore case and spaces).
# Example: 'racecar' → YES | 'hello' → NO

string = str(input("Enter string:")).lower().replace(" ","")
# first we need to remove all whitespaces and also convert into lowercase
print("Yes, Polindrome" if string == string[::-1] else "No, Not a Polindrome")