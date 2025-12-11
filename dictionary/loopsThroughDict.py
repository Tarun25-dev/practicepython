d={"name":"tarun","age":22,"branch":"computer science","college":"SREC","location":"Nandyal"}
#loop key
for key in d:
    print(key) #prints only keys

#loop key and values
for key,value in d.items(): # items() is a method which Returns all key-value pairs
    print(key,':',value)
