# STRING - A string is a sequence of characters inside quotes.
# Strings are Immutable, You cannot change a character inside a string.
# three type of quotes are used to represent strings
#1. " " --> double quotes - when write any long sentenses we use and also whenever  inside there is single quote we use double quotes
#2. ' ' --> single quotes - it is mainly used for small text or words and also whenever there is a double quotes inside that text then we use this for alternative 
#3. """ """ --> triple quotes -  which is used for mainly along paragraphs or multiple lines of text.
# Use ' ' when your string contains " " inside
# Use " " when your string contains ' ' inside
# Otherwise → you can choose any, both work the same

#-->syntax
name="THARUN KUMAR"
age="i'm 22 years old"
branch='computer science and engineering("ds")'
print(f"{name}\n{age}\n{branch}")

#-->adding two strings is  called string concatination by using (+) symbol
firstname="Tharun"
lastname="kumar"
fullname=firstname+" "+lastname
print(fullname)

#-->accessing strings through calling index value
college="SANTHIRAM ENGINEERING COLLEGE"
print(college[0])
print(college[-1])
