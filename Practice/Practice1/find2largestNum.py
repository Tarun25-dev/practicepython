li=[10,20,30,40,50,30,24,39,49,220]
li=list(set(li)) # which removes dup value first it converts into set and then convert again into list.
for i in range(2): # why 2 here means each i iteration keep one big value at last first i iteration keeps largest element keep at last and then second largest so we dont need further to sort we get that in the index of -2
    for j in range(len(li)-1):
        if li[j] > li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print(li[-2])

# 2 best for test
arr=[10,20,30,40,50,60,70,40,32,54,76,22,89]
largest=float('-inf') # we set a value that value is the lowest value as compared to in list so we can easily do for all numbers for positive and negative
second=float('-inf') # inf means infinity
for num in arr:
    if num > largest:
        second = largest
        largest=num
    elif num < largest and num > second: # here that the num value is < largest but > second so we dont need to distrub the value in largest we do only replace num with second.
        second=num
print(second)
      


