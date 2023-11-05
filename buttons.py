from tkinter import *
from customtkinter import *

#shaping the app window
app = CTk()
app.geometry("400x600")
app.title("Calculator")

set_appearance_mode("light")

#entrybox
entry1 = CTkEntry(master=app, width=359, height=160, state="disabled", corner_radius=30, fg_color="#D9D9D9", text_color="#000000", font=("Finger paint", 24), border_color="#D9D9D9")
entry1.pack(pady=20, padx=20)
entry1.place(x = 19, y = 31)

#default button
class DefaultButton:
        
        button = CTkButton(master=app, width=87, height=63, corner_radius=30, text_color="#000000", fg_color="#D9D9D9", font=("Finger paint", 24), text = (""))
        button.pack(pady=20, padx=20)
        button.place(x = 21, y = 203)

btn_1 = DefaultButton


app.mainloop()