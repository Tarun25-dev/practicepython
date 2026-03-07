# Given an array with only 0s, 1s, and 2s, sort it in one pass without using sort().

li=[0,1,2,0,1,2,1]
c0,c1,c2 = li.count(0),li.count(1),li.count(2)
li=[[0]*c0 + [1]*c1 + [2]*c2]
print(li)