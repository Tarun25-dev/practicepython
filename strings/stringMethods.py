#-->String Methods
s=" hello world "
print(s.upper()) # HELLO WORLD --> convert to uppercase
print(s.lower()) # hello world --> convert to lowercase
print(s.title()) # Hello World --> First letter capital of each word
print(s.strip()) #hello world --> it removes the unwanted spaces at starting and last spaces in strings
print(s.replace("world","python")) # hello python -->(text that want to replace, with this text)
#--> When you use split() in Python, extra spaces at the beginning or end of the string are automatically removed during splitting.
print(s.split()) #['hello', 'world'] --> Convert string to list
# join() --> syntax: separator.join(list)
#separator --> what you want between each element
# list --> the elements to combine (must be strings)
li=["tharun","kumar","kodiganti"]
print("$".join(li)) #tharun$kumar$kodiganti
print(" ".join(li)) #tharun kumar kodiganti
print("_".join(li)) #tharun_kumar_kodiganti

