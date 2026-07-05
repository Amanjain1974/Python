import tkinter as tk
import tkinter.font as tfont


window = tk.Tk()
window.title("My application")
window.minsize(width=400 ,height =300)

label =tk.Label(text="Hello world \n\n have a nice day")
label.config(font=("Roman",25))

label.pack()

window.mainloop()
