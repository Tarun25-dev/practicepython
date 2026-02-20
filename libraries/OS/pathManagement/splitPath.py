# The os.path.split() function splits a path into two parts:

# (head, tail)
# head → The directory path (everything before the last slash)
# tail → The last part of the path (file or folder name)
# head, tail = os.path.split(path)

# path → The full path you want to split.

# Returns a tuple (head, tail).

import os 
path = "C:\\Users\\THIS PC\\Desktop\\python\\OS\\CreatedByOS"
print(os.path.split(path)) # ('C:\\Users\\THIS PC\\Desktop\\python\\OS', 'CreatedByOS')

