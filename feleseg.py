from tkinter import *
from tkinter import ttk
import tkinter as tk
win = Tk()
entry = Entry(win, width= 42)
def get_data():
    entered_text = entry.get().strip()
    if not entered_text or entered_text == placeholder:
        label.config(text="Először írj be nevet!", fg='red')
    elif len(entered_text.split()) < 2:
        label.config(text="A teljes nevedet írd be!", fg='red')
    else:
        labeltext = "A feleséged neve: " + entered_text + "né"
        label.config(text=labeltext, fg='black')
def on_entry_click(event):
    if entry.get() == placeholder:
        entry.delete(0, "end")
        entry.config(fg='black')
def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, placeholder)
        entry.config(fg='grey')
win.geometry("700x250")
win.title("Feleség név kitaláló")
placeholder = "Teljes neved"
entry.place(relx= .5, rely= .5, anchor= CENTER)
entry.insert(0, placeholder)
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
label= Label(win, text="", font=('Helvetica 11'))
label.pack()
ttk.Button(win, text= "OK", command= get_data).place(relx= .7, rely= .5, anchor= CENTER)
win.iconphoto(False, tk.PhotoImage(file="C:\Program Files\Szponer\kitalalo\icon.png"))
win.mainloop()