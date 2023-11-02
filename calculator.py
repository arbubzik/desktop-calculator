from customtkinter import *

#shaping the app window
app = CTk()
app.geometry("400x600")
app.title("Calculator")

set_default_color_theme("dark-blue")
#button

btn = CTkButton(master=app, width=87, height=63, corner_radius=32, text="(")

btn.pack(pady=20, padx=20)
btn.place(x = 21, y = 203)
#starting the app
app.mainloop()