def pow(num):
    if num==1:
        return True
    if num<=0 or num%3!=0:
        return False
    return pow(num//3)
if pow(27)==True:
    print("is a power of three")
else:
    print("not a power of three")