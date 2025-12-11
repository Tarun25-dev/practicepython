# Adding / updating items in dictionary
dt={"name":"tarun","age":22,"branch":"computer science","college":"SREC","location":"Nandyal"}
dt["status"]="pursuing" # adding new value
dt["name"]="Tharun Kumar" # updating an existing value
print(dt)

# remove items from dictionary
d={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
d.pop('f')
print(d) #{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(d.pop('i','not found')) #not found
d['g']=7
print(d)
d.popitem() #deletes last item
print(d)
d.clear() # which deletes entire dictionary 
print(d)  # returns an empty dictionary

