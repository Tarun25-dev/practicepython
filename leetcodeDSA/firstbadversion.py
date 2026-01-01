# First bad version
# once a bad version comes, all after it are also bad
# you must find the first index of bad version
# here 0=Good, 1=Bad

versions=[0,0,0,0,1,1,1]
low=0
high=len(versions)-1
first_bad=-1 # if no bad found then it returns -1
while low <= high:
    mid=(low+high)//2
    if versions[mid]==1:
        first_bad=mid
        high=mid-1
    else:
        low=mid+1
print(first_bad)