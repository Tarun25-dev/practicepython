li=[4,3,6,2,6,9,5,4,10]
windowSize=int(input("Enter window size:"))
if windowSize <=0 or windowSize > len(li):
    print("Invalid window size:",windowSize)
    exit()
windowMaxsum=0
for i in range(windowSize):
    windowMaxsum+=li[i]
windowSum=windowMaxsum
for i in range(windowSize,len(li)):
    windowSum=windowSum-li[i-windowSize]+li[i] # new_sum=oldSum-first_element+next_element this means adding next element and simultaneously removing old sum first element
    if windowSum > windowMaxsum:
        windowMaxsum=windowSum
print(windowMaxsum)
    
