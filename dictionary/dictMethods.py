#-->keys() - Returns all keys
#-->values() - Returns all values
#-->items() - Returns all key-value pairs
#-->update() - used for add key values or update those 
d={"name":"tarun","age":22,"branch":"computer science","college":"SREC","location":"Nandyal"}
print(d.keys()) # dict_keys(['name', 'age', 'branch', 'college', 'location'])
print(d.values()) # dict_values(['tarun', 22, 'computer science', 'SREC', 'Nandyal'])
print(d.items()) # dict_items([('name', 'tarun'), ('age', 22), ('branch', 'computer science'), ('college', 'SREC'), ('location', 'Nandyal')])
# syntax dict.get(key,default_value)
print(d.get("name"))
print(d.get("age","not found"))
# key → the key you want the value for
# default_value → optional, returned if key is missing
d.update({"district":"Nandyal","status":"pursuing"})
print(d)
# Using keyword arguments
d.update(name="Tharun kumar",age=23)
print(d)