import tkinter as tk
root=tk.Tk() # creates a window object
entry=tk.Entry(root) # Entry() is used to take text input field.
entry.pack() # makes it visible in window
label=tk.Label(root)
label.pack()
def show():
    label.config(text=entry.get()) # which takes the text from, input field using get() method
btn=tk.Button(root,text="click",command=show)
btn.pack()
root.mainloop()
