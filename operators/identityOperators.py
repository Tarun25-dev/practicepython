#Check if two variables reference the same object.
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)      # True (same object)
print(x is z)      # False (different objects)
print(x is not z)  # True
