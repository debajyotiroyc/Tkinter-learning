from tkinter import *
import tkinter.messagebox as tmsg
def click():
    msg=tmsg.showinfo("INFO","Are you done?")
    print(msg)
    a=tmsg.askquestion("Rate","Works correct?")
    print(a)
    b=tmsg.askokcancel("Connect","Want to connect with us?")
    print(b)
    b = tmsg.askretrycancel("Connect", "Want to connect with us?")
    print(b)
    b=tmsg.showerror("Error","Look for errors.")
    print(b)
root=Tk()
root.title("GUI WINDOW")
menubar=Menu(root)

m1=Menu(menubar,tearoff=0)
m1.add_command(label="One",command=click)
m1.add_command(label="Two",command=click)
menubar.add_cascade(label="First",menu=m1)

m2=Menu(menubar,tearoff=0)
m2.add_command(label="Three",command=click)
m2.add_command(label="Four",command=click)
menubar.add_cascade(label="Second",menu=m2)
root.config(menu=menubar)
root.mainloop()