from tkinter import *
def fun():
    print("Done")
root=Tk()
root.title("MENUS AND SUBMENUS")
menubar=Menu(root)
m1=Menu(menubar,tearoff=0)
m1.add_command(label="New Project",command=fun)
m1.add_command(label="Save",command=fun)
m1.add_command(label="Show",command=fun)
menubar.add_cascade(label="First",menu=m1)

m2=Menu(menubar,tearoff=0)
m2.add_command(label="Help",command=fun)
m2.add_command(label="Info",command=fun)
m2.add_separator()
m2.add_command(label="Quit",command=fun)
menubar.add_cascade(label="Second",menu=m2)

root.config(menu=menubar)
root.mainloop()
