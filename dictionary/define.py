# Dictionary - A dictionary is a collection of key–value pairs.
# Each key is unique, but values can be repeated.
# Before Python 3.7 → dictionaries were unordered
# Order of keys was not guaranteed.
# Python 3.7 and later → dictionaries preserve insertion order
# Keys appear in the order you added them, but they are still not indexed like lists.
# Uses {} to create
# each key values can be seperated by colon(:) and each pair is seperated by comma(,)
dt={"name":"Tharun","age":22,"college":"SREC"}
print(dt,type(dt)) #{'name': 'Tharun', 'age': 22, 'college': 'SREC'} <class 'dict'>

dictionary=dict(name="Tharun",age=22,college="SREC") #some changes we dont need quotes for keys and also instead of colon we use equals(=) symbol
print(dictionary,type(dictionary))

#-->Accessing values form dictionary

d={"name":"tarun","age":22,"branch":"computer science","college":"SREC","location":"Nandyal"}
print(f"my name is {d['name']} and i'm {d['age']} years old. Currently studying bachlor's degree in {d['college']}, stream of {d['branch']} and i'm from {d['location']}.")
