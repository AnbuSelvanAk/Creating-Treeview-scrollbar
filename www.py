from tkinter import *
from tkinter import ttk
a=Tk()
a.resizable(width=1,height=1)
t=ttk.Treeview(a)
t.pack(side='top')
v=Scrollbar(a,orient="vertical",command=t.yview)
v.pack(side='right',fill='x')
t.configure(xscrollcommand=v.set)
t["columns"]=("1","2","3")
t['show']='headings'
t.column("1",width=90)
t.column("2",width=90)
t.column("3",width=90)
t.heading("1",text="student name")
t.heading("2",text="age")
t.heading("3",text="place")
t.insert("",'end',text="L1",values=("anbu","21","trichy"))
t.insert("",'end',text="L1",values=("rohit","25","chennai"))
a.mainloop()