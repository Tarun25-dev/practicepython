#For loop - Used when you know how many times to repeat.
first=int(input("enter starting value:"))
last=int(input("enter end value:"))
count=0
totalSum=0
if first<last:
    for i in range(first,last+1):
        if i%2==0:
            print(i)
            count+=1
            totalSum+=i
    print("total number of even values are:",count)
    print("total sum of even values are:",totalSum)
else:
    print("starting value must be < end value and also end value not be lessthan starting value")
