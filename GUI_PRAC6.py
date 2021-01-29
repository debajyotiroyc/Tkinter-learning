from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.title("RadioButton Window")

def place():
    tmsg.showinfo("Place",f"You are from {var.get()}")

Label(root,text="Where are you from?",font="arial 20 bold",fg="blue",bg="red").pack(side=TOP,padx=5)
lst=["India","USA","England","Japan","Egypt","Brazil"]
var=StringVar()
var.set("Radio")
for i in lst:
    Radiobutton(root,text=i,padx=5,variable=var,value=i).pack(side=TOP,anchor="w")
Button(root,text="Submit",command=place).pack(anchor="w")


root.mainloop()