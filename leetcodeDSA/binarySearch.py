li=[10,20,30,40,50,60,70,80,90]
target=int(input("enter taget value:"))
found=False
for i in range(len(li)):
    if li[i]==target:
        print("Element found at  index:",i)
        found=True
        break
if not found:
    print("not found element ",target)