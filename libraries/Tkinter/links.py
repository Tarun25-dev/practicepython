import tkinter as tk
import webbrowser # Built-in Python module (import webbrowser) Lets you open a URL in the default web browser.
def openlink():
    webbrowser.open("www.youtube.com")
root=tk.Tk()
link=tk.Label(root,text="Youtube",fg="blue",cursor="hand2")
link.pack()
link.bind("<Button-1>",lambda e:openlink()) # button -1 is an event which does to run the function when we click left mouse button.
root.mainloop()