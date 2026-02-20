# we need to verify that the file is exist in the system or not by using os.path.exists() method
import os
path = "C:\\Users\\THIS PC\\Desktop\\python\\OS" # we can verify wether os folder exists or not 
print(os.path.exists(path)) # True
print(os.path.exists("C:\\Users\\THIS PC\\Desktop\\python\\Day")) # False