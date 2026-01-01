li=[-4,-1,0,3,10]
result=[0]*len(li)
left=0 # highest negative value
right=len(li)-1 # highest positive value
pos=len(li)-1
while left<=right:
    if abs(li[left]>abs(li[right])):
        result[pos]=li[left]*li[left]
        left+=1
    else:
        result[pos]=li[right]*li[right]
        right-=1
    pos-=1
    print(result)
print(result)