# if you want to change current dir path then use this method called .chdir(path)
import os
# before path is "C:\Users\THIS PC\Desktop\python\OS"
os.chdir("C:\\Users\\THIS PC\\Desktop\\python")
# why we use double backslashes in python single \ is treated as escape charecter so thats why we use \\.
print(os.getcwd()) # C:\Users\THIS PC\Desktop\python
