# first loop -> climbs up
# stops exactly at peak and also peak value must single 
# if checks whether the i value is 0 or 1 then immediately stop the code beacuse valid mountain doesnt has length zero or one 
# second loop climbs down
# if i value reached sucessfully at the end of the index then it is a valid mountain otherwise not a valid mountain.

li=[1,2,3,4,5,6,5,4,3,2,1,0]
i=0
if len(li)<3:
    print("valid mountain must have atleast 3elements")
while i+1 < len(li) and li[i] < li[i+1]: # i+1 is used to reduce the outofrange error if i+1 is greater then it stops the loop.
    i+=1
if i==0 or i==len(li)-1:
    print("not a valid mountain")
    exit()
while i+1 < len(li) and li[i] > li[i+1]:
    i+=1
if i==len(li)-1:
    print("is_valid mountain")
else:
    print("not a valid mountain")