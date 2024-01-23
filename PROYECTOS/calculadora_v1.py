from tkinter import *



root=Tk()


root.title = "CALCULADORA"

#root.geometry ("")




Button(root, text='1', command=None).grid(row=1, column=0)
Button(root, text='2', command=None).grid(row=1, column=1)
Button(root, text='3', command=None).grid(row=1, column=2)
Button(root, text='4', command=None).grid(row=2, column=0)
Button(root, text='5', command=None).grid(row=2, column=1)
Button(root, text='6', command=None).grid(row=2, column=2)
Button(root, text='7', command=None).grid(row=3, column=0)
Button(root, text='8', command=None).grid(row=3, column=1)
Button(root, text='9', command=None).grid(row=3, column=2)
Button(root, text='0', command=None).grid(row=4, column=0)
Button(root, text='=', command=None).grid(row=4, column=1)











root.mainloop()