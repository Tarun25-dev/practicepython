"""Maximum Subarray
Find the contiguous subarray with the largest sum.
"""
li=[10,20,30,40,12,43,25,99,56,85]
windowSize=int(input("Enter size of window:"))
if windowSize<=0 or windowSize>len(li):
    print("invalid windowSize value")
    exit()
windowMaxSum=0
for i in range(windowSize):
    windowMaxSum+=li[i]

windowSum=windowMaxSum
for i in range(windowSize,len(li)):
    windowSum=windowMaxSum-li[i-windowSize]+li[i]
    
    if windowSum>windowMaxSum:
        windowMaxSum=windowSum
print(windowMaxSum)
    