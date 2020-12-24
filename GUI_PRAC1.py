from tkinter import *
def hello():
    print("hello drc!!")
def heal():
    print("you are fine and still the best in the world!!!!")

root=Tk()
root.geometry("500x500")
f1=Frame(root,bg="blue",borderwidth=10,relief=SUNKEN)
f1.pack(side=TOP,fill="x")
L=Label(f1,text="WELCOME TO PYCHARM ",font="Arial 15 bold",bg="red")
L.pack(side=TOP,fill=X)
f2=Frame(root,borderwidth=5,relief=SUNKEN,bg="black")
f2.pack(side=LEFT)
b1=Button(f2,text="Hello",fg="blue",bg="yellow",command=hello)
b1.pack(side=LEFT)
b2=Button(f2,text="Health",fg="green",bg="blue",command=heal)
b2.pack(side=LEFT)


root.mainloop()
