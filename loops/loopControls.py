#break - stops loop immediately
for i in range(10):
    if i==2:
        break
    print(i)


#continue - skips the current iteration
for j in range(20):
    if j==5:
        continue
    print(j) #here 5 number skips when the loop in 5 


#pass - does nothing
condition=10
if condition:
    pass  # do nothing for now later we implement that code
