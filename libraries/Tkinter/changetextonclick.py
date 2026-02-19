import tkinter as tk
root=tk.Tk() # creates a main window
label=tk.Label(root,text="before click...")
label.pack()
def click():
    label.config(text="After click...")
btn=tk.Button(root,text="click",command=click)
btn.pack()
root.mainloop()