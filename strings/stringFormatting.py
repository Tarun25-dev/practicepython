# mainly three types of formatting the string
#1. f-string --> best and modern way  to use
role="python developer"
lpa=25
print(f"my role is {role} and i got {lpa}Lpa") # my role is python developer and i got 25Lpa

#2. format() --> built-in method in python
print("my role is {} and i got {}Lpa".format(role,lpa)) # my role is python developer and i got 25Lpa

#3. % formatting --> old way
print("my role is %s and i got %dLpa" % (role,lpa)) # my role is python developer and i got 25Lpa
