import urllib.request
from tkinter import *
import tkinter as tk
window=Tk()

window.geometry("700x350")
window.title("Site Connectivity Checker")
head=Label(window, text="Website Connectivity Checker", font=('Calibri 15'))
head.pack(pady=20)

def check():
    web= (url.get())
    status_code = urllib.request.urlopen(web).getcode()
    website_is_up = status_code == 200
    if website_is_up==TRUE:
        Label(window, text="Website is Available", font=('Calibri 15')).place(x=260,y=200)
    else:
        Label(window, text="Website is Not Available", font=('Calibri 15')).place(x=260,y=200)

url=tk.StringVar()
Entry(window,bg="yellow", textvariable=url).place(x=200,y=80,height=30,width=280)
Button(window,bg='skyblue', text="Check",command=check).place(x=320,y=160)
window.mainloop()
