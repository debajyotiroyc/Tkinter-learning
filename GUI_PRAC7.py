from tkinter import *

root=Tk()
root.title("Scrollbar")
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
text=Text(root,yscrollcommand=scrollbar.set,height=100)
text.pack(fill=BOTH)
scrollbar.config(command=text.yview)
root.mainloop()