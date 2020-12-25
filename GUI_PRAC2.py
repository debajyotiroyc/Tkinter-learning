from tkinter import *
def getv():
    print(f"The username is : {user_val.get()}")
    print(f"The password is : {pass_val.get()}")

root=Tk()
user=Label(root,text="Username: ")
passw=Label(root,text="Password: ")
user.grid(row=0,column=0)
passw.grid(row=1,column=0)

user_val=StringVar()
pass_val=StringVar()

user_enter=Entry(root,textvariable=user_val)
pass_enter=Entry(root,textvariable=pass_val)

user_enter.grid(row=0,column=1)
pass_enter.grid(row=1,column=1)

Button(root,text="Submit",command=getv).grid(row=3,column=2)

root.mainloop()
