import os
path = 'C:\\Users\\THIS PC\\Desktop\\python\\OS\\Define.txt'
print(os.path.splitext(path)) # ('C:\\Users\\THIS PC\\Desktop\\python\\OS\\Define', '.txt')
tupl = os.path.splitext(path)
print(tupl[1]) # .txt