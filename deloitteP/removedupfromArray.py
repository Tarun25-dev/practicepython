arr=[10,20,30,40,20,10,30,56,44,79,54,54] # this approache may take first occurenes as main element and causes changes order why beacuse we comes from right to left
for i in range(len(arr)-1,-1,-1):
    for j in range(i-1,-1,-1):

        if arr[i] == arr[j]:
            del arr[j]
            break # inner loop breaks only if same 
print(arr)

# 2 best
arr1=[10,20,30,40,20,10,30,56,44,79,54,54]
seen = set() # created a set object 
unique=[]
for i in arr1:
    if i not in seen:
        seen.add(i) # takes only uniuqe elements so that only we append in uniue list
        unique.append(i)
print(unique)

# 3
arr2=[10,20,30,40,20,10,30,56,44,79,54,54]
arr3=[]
for i in arr2:
    if i not in arr3:
        arr3.append(i)
print(arr3)

# 4
arr4=[10,20,30,40,20,10,30,56,44,79,54,54]
print(list(set(arr4))) #this maay changes order


