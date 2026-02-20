import os
file = os.path.isfile("C:\\Users\\THIS PC\\Desktop\\python\\OS\\workingWithFiles\\filesExistsOrNot.py")
# we need to give fullfile name with extension also otherwise it treated as folder.
if file:
    print("File Exists")
else:
    print("Not exists or wrong path")
# File Exists