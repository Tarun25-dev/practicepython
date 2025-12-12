# List comprehension is a shortcut to create a list in one line.
# Instead of using a for loop to build a list, you can use list comprehension to do it neatly.
# Basic syntax: [expression for item in iterable if condition]

# expression → what you want to put in the new list (e.g., x*2)
# item → variable that represents each element of the original list
# iterable → list, range, string, etc.
# condition → optional, to include only certain elements 

li1=[1,2,3,4,5,6]
result=[x*x for x in li1]
print(result) #[1, 4, 9, 16, 25, 36]
result2=[x*x for x in li1 if x%2==0] #it allows only even numbers to multiply
print(result2) #[4, 16, 36]

# converts str to int
li2=["1","2","3","4","5"]
num=[int(x) for x in li2]
print(type(num[0])) #<class 'int'>

# Using functions in comprehension
li3=[1,2,3,4,5,6,7]
def double(x):
    return x+x
sum=[double(x) for x in li3]
print(sum) #[2, 4, 6, 8, 10, 12, 14]
