heights=[1,1,4,2,1,3,6,5]
result=sorted(heights)
misMatch=0
for i in range(len(heights)):
    if heights[i]!=result[i]:
        misMatch+=1
print(misMatch)