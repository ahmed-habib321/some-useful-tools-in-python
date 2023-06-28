from tkinter import *

frm = Tk()
menubar = Menu(frm)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label=' New ', command=lambda: print(' New '))
filemenu.add_command(label=' Save ', command=lambda: print(' Save '))

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label=' Copy ', command=lambda: print(' Copy '))
editmenu.add_command(label=' Cut ', command=lambda: print(' Cut '))


menubar.add_cascade(label=' File ', menu=filemenu)
menubar.add_cascade(label=' Edit ', menu=editmenu)
frm.config(menu=menubar)

frm.mainloop()
