# we can list out all the files and directories inside a main directory so we just need to give path for which folder you want to get the list
# py provides to do this type of function called .listdir()
# .listdir(.) it gives current dir files and folders inside 
# .listdir(..) it go back to current folder and gives all the files inside that dir
# .listdir(path = "C:\\Users\\THIS PC\\Desktop\\python")
import os
path = "C:\\Users\\THIS PC\\Desktop\\python\\OS"
print(os.listdir(path))
# ['CreatedByOS', 'Define.txt', 'osLib.txt', 'workingWithDirectories.py']