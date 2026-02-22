import tkinter as tk
root=tk.Tk()
# on terminal
"""


def say_hello():
    print("Hello Tkinter") # this prints in terminal or console not in window if we want it in window then we use config method
btn=tk.Button(root,text="click Me",command=say_hello) # command makes action when click the button and also we dont call the function like this say_hello() wrong
btn.pack() #this button keep that in main window
root.mainloop() #keep window running


"""
# on window
label=tk.Label(root,text="") # this creates a empty text on window we use this label in button function
label.pack() # which keeps that label in the main window
def hello():
    label.config(text="hello tkinter")
btn=tk.Button(root,text="clickme",command=hello)
btn.pack()
btn.mainloop()
