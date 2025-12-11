#slicing - extracting a portion of a list, string, or tuple without modifying the original.
#sequence[start : stop : step]
#start → index to start (inclusive)
#stop → index to stop (exclusive)
#step → how many steps to jump (optional)

names=["kodiganti","tharun","kumar","nani"]
print(names[0:3]) #["kodiganti","tharun","kumar"]
numbers=[1,2,3,4,5,6]
print(numbers[0:5:2]) #takes second element
print(numbers[:3]) #it prints from starting to index 3 exclusive means takes before 3
print(numbers[2:])
print(numbers[::-1]) #it starting from reverse #[6, 5, 4, 3, 2, 1]
print(numbers[0::-1]) #it starts with zero index and next move to last element (-1) and then stops beacuse it goes in wrong way

# Important Rule
# When step is negative, Python expects: 
# start index > stop index
#Otherwise, Python cannot move backward and the result is empty list.

print(numbers[0:5:-1]) #[] empty list

