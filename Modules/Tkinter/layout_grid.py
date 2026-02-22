import tkinter as tk
root=tk.Tk()
tk.Label(root,text="Name").grid(row=0, column=0) #grid is used for a location to move where we desire | row 0 | Name | Entry |
entry=tk.Entry(root)
entry.grid(row=0,column=1) # this input field place at row 0 means where the label there menas label side and also which is at location of column 1 
tk.Button(root,text="submit").grid(row=1,column=1) # place this under row 0 means row 1 and also at column 1 means exactly under input field
root.mainloop()
