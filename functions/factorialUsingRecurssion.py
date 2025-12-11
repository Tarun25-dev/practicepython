def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
num=int(input("enter a number :"))
print("factorial of ",num," is :",fact(num))