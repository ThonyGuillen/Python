import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()



ttk.Button(frm, text="1").grid(column=0, row=0)
ttk.Button(frm, text="2").grid(column=2, row=0)
ttk.Button(frm, text="3").grid(column=4, row=0)
ttk.Button(frm, text="+").grid(column=6, row=0)

ttk.Button(frm, text="4").grid(column=0, row=1)
ttk.Button(frm, text="5").grid(column=2, row=1)
ttk.Button(frm, text="6").grid(column=4, row=1)
ttk.Button(frm, text="-").grid(column=6, row=1)

ttk.Button(frm, text="7").grid(column=0, row=2)
ttk.Button(frm, text="8").grid(column=2, row=2)
ttk.Button(frm, text="9").grid(column=4, row=2)
ttk.Button(frm, text="*").grid(column=6, row=2)

ttk.Button(frm, text="0").grid(column=2, row=3)
ttk.Button(frm, text="/").grid(column=6, row=3)


#ttk.Label(frm, text="SUMA").grid(column=0, row=0)
#ttk.Button(frm, text="+", command=root.destroy).grid(column=1, row=0)

#ttk.Label(frm, text="Resta").grid(column=0, row=1)
#ttk.Button(frm, text="-", command=root.destroy).grid(column=1, row=1)

#ttk.Label(frm, text="Multiplicion").grid(column=0, row=2)
#ttk.Button(frm, text="*", command=root.destroy).grid(column=1, row=2)

#ttk.Label(frm, text="Divicion").grid(column=0, row=3)
#ttk.Button(frm, text="/", command=root.destroy).grid(column=1, row=3)

root.mainloop()