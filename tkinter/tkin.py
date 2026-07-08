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

# sepration line between the elements
sep = ttk.Separator(orient="horizontal")
sep.pack(fill= 'x')


text =tk.Text(height=25 ,width=25)
text.pack()
text.focus()

# default text
text.insert(index= "1.0",chars="enter you comments")

# to print output on console 
def text_function():
    text_data = text.get(index1="1.0",index2="end")
    print(text_data)

text_button = ttk.Button(text="get text",command =text_function)
text_button.pack()

# text["state"] = "disabled"

# def enable_text():
#     text["state"] = "normal"

# # adding an button to enable the comment section

# enable_button = ttk.Button(text = "Enable Text Box",command =enable_text)
# enable_button.pack()    

# check button

check_option =tk.IntVar()

def check_option_task():
    print(check_option.get()) 

check_button = ttk.Checkbutton(text="Agree with the terms and conditions",variable =check_option,
                               command=check_option_task)
check_button.pack()

# radio button in which you can only select only one value

radio_value =tk.StringVar()
option_1 =ttk.Radiobutton(text ="Male",variable =radio_value,value ="male")
option_2 =ttk.Radiobutton(text ="Female",variable =radio_value,value ="Female")

option_1.pack()
option_2.pack()

# combobox
selected_country =tk.StringVar()
countries = ttk.Combobox(textvariable= selected_country,values=("Australia","Canada","India","Pakistan","Banglades"))
countries["state"] ="readonly"
countries.pack()

def display_country(event):
    print(f"selected country is {selected_country.get()}")

countries.bind("<<ComboboxSelected>>",display_country)

# listbox
food_items =("Pizza","Burger","Garlic Bread","Nachos","Salad")
fav_food=tk.StringVar(value =food_items)

food_list = tk.Listbox(listvariable=fav_food,height =5)
food_list.pack()

# Spinbox

counter =tk.IntVar(value =10)
spin_box = ttk.Spinbox(from_=0,to=20,textvariable=counter,wrap=True)

spin_box.pack()

window.mainloop()
