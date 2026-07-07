import tkinter as tk
import tkinter.font as tfont
from tkinter import ttk


window = tk.Tk()
window.title("My application")
window.minsize(width=400 ,height =300)

label =tk.Label(text="Hello world \n\n have a nice day")
label.config(font=("Roman",25))

label.pack()
# label["text"] ="have a nice day"
# label.config(text ="My new App")
counter =0
def function_button():
    # print("Thanks For Clicking")
    label.config(text =f"The user input is {user_input}")

# taking user input using entry
user_input =tk.Entry(width =30,show = "*")
user_input.pack()


# buttons
button =tk.Button(text="click",command=function_button)
# this prints on console
button.pack()

# quit button
quit_button = ttk.Button(text="Quit",command= window.destroy)
quit_button.pack()


window.mainloop()
