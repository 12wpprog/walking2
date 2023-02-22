from tkinter import *

def demo1():
    root = Tk()
    root.option_add("*Font", "impact 25")
    Button(root,text="apple").pack(side=LEFT)
    Button(root,text="banana").pack(side=LEFT)
    Button(root,text="coconut").pack(side=LEFT)
    Button(root,text="tulip").pack(side=RIGHT)
    Button(root,text="papaya").pack(side=RIGHT)
 
    root.mainloop()

def demo2():
    root = Tk()
    root.option_add("*Font", "impact 25")
    Button(root,text="apple").pack()
    Button(root,text="banana").pack()
    Button(root,text="coconut").pack()
    Button(root,text="tulip").pack()
    Button(root,text="papaya").pack()
 
    root.mainloop()

if __name__  == '__main__':
    demo2()

