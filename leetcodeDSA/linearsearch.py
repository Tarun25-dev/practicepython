""" Linear Search
Find index of a target element in an array.
rules:
> start from first element
> compare one element at a time
> if match found then stop 
> if no match return not found
> no sorting required
> for using loops time complexity is O(n), and space complexity is O(1).
"""
li=[10,20,30,40,50,60,70,80,90]
target=int(input("Enter target value:"))
found=False
for i in range(len(li)):
    if li[i]==target:
        print(f"{target} is at index {i}")
        found=True
        break
if not found:
    print("No such element in list")

# method 2
i=0
is_found=False
while i<len(li):
    if li[i]==target:
        print("index:",i)
        is_found=True
        break
    i+=1
if not is_found:
    print("No such Element")

# method 3
if target in li:
    print("index:",li.index(target))
else:
    print("not found")