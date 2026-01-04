
n1=str(input("Enter First name:"))
n2=str(input("Enter second name:"))
n1=n1.replace(" ","").lower()
n2=n2.replace(" ","").lower() # this makes all names into lowercase and also if there are any spaces then it replaces with empty
li1=list(n1) # convert string to list and each char at stored as index wise
li2=list(n2)
for i in li1: # loop through first list
    if i in li2: # loop through second list
        li1.remove(i)
        li2.remove(i)
count=len(li1)+len(li2) #counting the letters after removing same elements in list
Flames=[1,2,3,4,5,6]
index=0 # where you are now currently on flames like pointer
while len(Flames)>1: # when len of flames has 1 then it fails the loop then only we get one letter that was the result.
    index = (index + count-1) % len(Flames) # % len(flames) it wraps back to the start. count-1 is for assume that we want fifth letter so that fifth letter is at index 4 so thats why we reduce one
    Flames.pop(index)
match Flames[0]:
    case 1:
        print("Friends 🤝")
        print('You are going to build a strong friendship with this person, full of trust and support.')
    case 2:
        print("Love ❤️")
        print('You are going to fall deeply in love, and this connection may turn into a beautiful relationship.')
    case 3:
        print("Affection 💖")
        print('You are going to share a lot of care, attention, and emotional closeness with this person.')
    case 4:
        print("Marriage 💍")
        print('You are going to have a serious bond that may lead to marriage and a lifelong commitment.')
    case 5:
        print("Enemies ⚔️")
        print('You are going to face misunderstandings or conflicts, so it’s better to be careful with emotions.')
    case 6:
        print("Sibling 👨‍👩‍👧")
        print('You are going to have a sibling-like bond, filled with teasing, care, and comfort.')
        
