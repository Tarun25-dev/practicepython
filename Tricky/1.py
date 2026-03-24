s="hello"
t=s # it takes as refernces it t changes then automatically s also change 
s=s.upper() #here we try to modify s by assigning same variable but py strings are immutable so it takes as a new variable that old variable s will automatically removes and then go to garbage
print(t) #here t value is old s so already it stored old strings="hello"
t=s # it takes refernce from s
s=s.upper() 
print(t)
