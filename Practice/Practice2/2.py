# Find second Largest element in array

li=[1,4,20,2,9,2,5,6,3,10,20]
largest = second = -float('inf') # we taken lowest element to compare with given list for all numbers from neg and pos
for num in li:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest: # which checks two conditions 
        # The number must be greater than the current second largest.
        # The number must not be equal to the largest number. beacuse it avoids duplicates like [10, 20, 20, 5] we know that answer is 10 but without this logic they consider second as 20 so to avoid it we take num ! = largest
        second = num
        
print(second)
       
# through sorting
li1= [10, 20, 20, 5]
# remove dup
li1=list(set(li1))
for i in range(len(li1)):
    for j in range(0,len(li1)-i-1):
        if li1[j]>li1[j+1]:
            li1[j],li1[j+1] = li1[j+1],li1[j] # over sorting
print(li1[-2])
