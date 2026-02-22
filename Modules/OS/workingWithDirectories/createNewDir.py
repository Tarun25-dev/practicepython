# by using python we can also create directories.
# For single directory we use method called .mkdir()
# it takes your current path and in that it create 
# so first you setup dir path and then create it.
import os
os.mkdir("CreatedByOS")
# or os.mkdir("C:\\Users\\THIS PC\\Desktop\\python\\OS\\CreatedByOS") also we can write like this.
# Creates a single directory.
# Fails if the parent directory does not exist.

# For this method .makedirs() which doesnt exits error if the folder already exists in a system for that it provides one property called exist_ok = False so if exists no error
os.makedirs("C:\\Users\\THIS PC\\Desktop\\python\\OS\\CreatedByOS",exist_ok=True)
