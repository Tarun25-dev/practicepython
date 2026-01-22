# Insertion sort - Take one element at a time and insert it into its correct position in the already sorted part.
# Example: [7,3,5,2]
# first 7 - ok  [7]
# second 3 - 3 is < 7 then put it before [3,7]
# third 5 - 5 is < 7 and also > 3 then put it between [3,5,7]
# fourth 2 - 2 < 7 and 5 and 3 so we move front of these three elements [2,3,5,7]
li=[7,3,5,2,9,1]
for i in range(1,len(li)):
    key=li[i]
    j=i-1 # 0 to len of list 
    while j >=0 and li[j] > key:
        li[j+1]=li[j]
        j-=1
    li[j+1]=key
    print(li)
# we add one new element that finds their actual position and place thats called insertion
        
        