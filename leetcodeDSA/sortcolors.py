# an array only contains zeros, ones, twos
# 0=red, 1=white, 2=blue
# you must sort it inplace without using extra space and sort method
colors=[2,1,0,2,1,1,0,2,1]
low=0 # where next zero should go
mid=0 # current index
high=len(colors)-1
while mid <= high:
    if colors[mid]==0:
        colors[low],colors[mid]=colors[mid],colors[low]
        low+=1
        mid+=1
    elif colors[mid]==1:
        mid+=1
    else:
        colors[mid],colors[high]=colors[high],colors[mid]
        high-=1
    print(colors)
print(colors)