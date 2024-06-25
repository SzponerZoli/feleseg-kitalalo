from tkinter import *
from tkinter import ttk
import tkinter as tk
def on_entry_click(event):
    if entry.get() == placeholder:
        entry.delete(0, "end")
        entry.config(fg='black')
def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='grey')
win = Tk()
win.geometry("700x250")
win.title("Feleség név kitaláló")
def get_data():
    if entry.get() == '' or entry.get() == placeholder:
        label.config(text="Először írj be nevet!", font= ('Helvetica 11'))
    else:
        label.config(text="A feleséged neve: " + entry.get() + "né", font= ('Helvetica 11'))
placeholder = "Teljes név"
entry = Entry(win, width= 42)
entry.place(relx= .5, rely= .5, anchor= CENTER)
entry.insert(0, placeholder)
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
label= Label(win, text="", font=('Helvetica 11'))
label.pack()
ttk.Button(win, text= "OK", command= get_data).place(relx= .7, rely= .5, anchor= CENTER)
win.mainloop()