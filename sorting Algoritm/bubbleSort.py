# Bubble sort is technique to sort all the elements in the list,
# repeatedly comparing two neighboring elements and swapping them if they are in the wrong order until the  whole list becomes sorted.
li=[10,2,3,13,4,32,45,23,54]
for i in range(len(li)):
    for j in range(0,len(li)-i-1):
        if li[j] > li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
print(li)