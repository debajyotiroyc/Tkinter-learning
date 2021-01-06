from tkinter import *

def event(e):
    Label(root,text=f"YOU CLICKED AT {e.x},{e.y}").pack()

root=Tk()
root.title("GUI WINDOW")
b=Button(root,text="Press",bg="blue",fg="red")
b.pack()
b.bind('<Button-1>',event)

root.mainloop()