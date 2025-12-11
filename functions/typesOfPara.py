#1. required parameters
def name(a,b):
    print(a,b)
    print(a-b)
    print(a*b)
    print(a/b)
name(9,10)

#2. default parameters
def name(Name="user"):
    print(Name)
name() #default value is user and when there is no argument while calling itself it taken default value as user
name("tharun") 

#3. multiple parameters
def main(name,age,branch):
    print(name,age,branch)
main("tharun",22,"computer science")
