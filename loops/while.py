#Used when you repeat until a condition becomes false.
import random
num=random.randint(1,10)
secretNum=10
guess=0
print("welccome to the guessing game")
while num!=secretNum:
    guess=int(input("Enter a number:"))
    if guess>num:
        print("Too High ! try again...")
    elif guess<num:
        print("Too low ! try again...")
    else:
        print("Congrats!..,Your the winner")


    