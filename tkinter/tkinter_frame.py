import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("My Application")

my_frame = ttk.Frame()
my_frame.pack(side ="left",fill ='both',expand =True)

label1 = tk.Label(text ="Hello World" ,bg ="red")
label1.pack(side="left",fill ='both',expand =True)

label2 = tk.Label(text ="How Are YOu ?" , bg= "green")

label2.pack(side = "left" ,fill ='both',expand =True)

label3 = tk.Label(text ="Have A Nice Day", bg ="blue")
label3.pack(side = "left" ,fill ='both',expand =True)


window.mainloop()