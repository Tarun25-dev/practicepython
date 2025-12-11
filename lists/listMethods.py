#List Methods
#1. Adding elements in list
list1 = [1,2,3]
list1.append(4) #append method add element at last of the list
list1.insert(0,0) #using insert method, adding 0 element in zero index
print(list1)

#2. removing elements from list
list2=['a','b','c','d','e']
list2.remove('e') #removing using value ['a', 'b', 'c', 'd']
print(list2)
list2.pop() #remove last  element ['a', 'b', 'c']
print(list2)
list2.pop(2)#['a', 'b']
print(list2)

#3. sorting in ascending order
list3=[9,8,6,5,3,6,2,7]
list3.sort()
print(list3)

#4. reverse  list
list4=[1,2,3,4,5,6]
list4.reverse()
print(list4)

#5. if we want decending order then first we use sort method for ascending order and then reverse that list which gives descending order
list5=[4,3,2,5,6]
list5.sort()
list5.reverse()
print(list5)

#6. find length of the list
list6=[5,3,6,2,6]

print(len(list6))
print(list6.count(6)) #it finds an element  how many times which appears in the tuple
print(list6.index(6)) #finding the index value according to the existing element in list
