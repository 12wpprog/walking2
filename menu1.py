from tkinter import *
from tkmacosx import Button



root = Tk()

root.option_add('*Font','Impact 25')

menus = ['mocha','latte','espresso']
colors = ['red','green','blue']

for i,m in enumerate(menus):
    Label(root,text=m,bg=colors[i],fg='white',border=2).pack(side=TOP,padx=10,pady=10)

root.mainloop()
