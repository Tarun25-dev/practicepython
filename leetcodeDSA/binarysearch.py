""" Binary Search
Search target in a sorted array using binary search.
rules:
> must be sorted before search
> time complexity : O(logn)
> space complexity : O(1)
"""
li=[10,90,20,30,80,40,70,50,60]
target=int(input("Enter target value:"))
for i in range(len(li)):
    for j in range(i+1,len(li)):
       if li[i]>li[j]:
           li[i],li[j]=li[j],li[i]
left=0
right=len(li)-1
found=False
while left <= right:
    mid=left + (right-left)//2 # this prevents overflow but this formula stops that overflow
    # how means if we directly do that right - left // 2 whenever there is bigger numbers first left//2 is calculated and then that value is substracted by right which causes to exceeds the limit of an integer
    # if we use this formula first do the operation between () and then it reduces already then again we divide with floor division then the value becomes more decreases after that we add the left value what we removed first operation.
    # both are gives same mid value but for overflow edge case we prefer this method.
    if li[mid] == target:
        print("Target value is at index:",mid)
        found=True
        exit()
    elif li[mid]<target: #right portion
        left=mid+1
    else:
        right=mid-1
if not found:
    print("Given element is not in a list")

