""" Reverse String
Given a character array, reverse it in-place.
"""
li=["T","H","A","R","U","N"]

#method 1
li.reverse()
print(li)

#method 2
start=0
end=len(li)-1
while start < end:
    li[start],li[end]=li[end],li[start]
    start+=1
    end-=1
print(li)

#method 3
print(li[::-1])

