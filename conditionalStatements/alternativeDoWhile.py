# Why python doesnt has do while - beacuse, A do-while loop is not strictly necessary because the same behavior can be achieved using while.
# we acheive same functionality using while loop only
# means must be execute expression then after conditions comes into play
while True:
    num=int(input("Enter a number"))
    if num<0:
        print("must be greaterthan zero")
    else:
        print("input number is:",num) 
        break

# Task 
pwd="tarun123"
attempt=0
while True:
    password=input("Enter Password: ")
    if password == pwd:
        print("Access Granted")
        break
    else:
        attempt+=1
        if attempt==3:
            print("access locked")
            break
        else:
            print("Password Incorrect")