import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
name1=tk.Label(root,text="Name 1:").grid(row=0,column=0)
name2=tk.Label(root,text="Name 2:").grid(row=1,column=0)
iname1=tk.Entry(root)
iname1.grid(row=0,column=1)
iname2=tk.Entry(root)
iname2.grid(row=1,column=1)
def play():
    n1=iname1.get()
    n2=iname2.get()
    n1=n1.replace(" ","").lower()
    n2=n2.replace(" ","").lower()
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
            messagebox.showinfo(title="Friends 🤝",message='You are going to build a strong friendship with this person, full of trust and support.')
        case 2:
            messagebox.showinfo(title="Love ❤️",message='You are going to fall deeply in love, and this connection may turn into a beautiful relationship.')
        case 3:
            messagebox.showinfo(title="Affection 💖",message="You are going to share a lot of care, attention, and emotional closeness with this person.")
        case 4:
            messagebox.showinfo(title="Marriage 💍",message="You are going to have a serious bond that may lead to marriage and a lifelong commitment.")
        case 5:
            messagebox.showwarning(title="Enemies ⚔️",message="You are going to face misunderstandings or conflicts, so it’s better to be careful with emotions.")
        case 6:
            messagebox.showinfo(title="Sibling 👨‍👩‍👧",message="You are going to have a sibling-like bond, filled with teasing, care, and comfort.")

btn=tk.Button(root,text="Play",command=play).grid(row=0,column=2,rowspan=2)
root.mainloop()


