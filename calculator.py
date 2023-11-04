from customtkinter import *

#shaping the app window
app = CTk()
app.geometry("400x600")
app.title("Calculator")

set_default_color_theme("dark-blue")

#button_1 is (
btn_1 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="(")
btn_1.pack(pady=20, padx=20)
btn_1.place(x = 21, y = 203)

#button_2 is )
btn_2 = CTkButton(master=app, width=87, height=63, corner_radius=32, text=")")
btn_2.pack(pady=20, padx=20)
btn_2.place(x = 112, y = 203)

#button_3 is %
btn_3 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="%")
btn_3.pack(pady=20, padx=20)
btn_3.place(x = 202, y = 203)

#button_4 is AC
btn_4 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="AC")
btn_4.pack(pady=20, padx=20)
btn_4.place(x = 293, y = 203)

#button_5 is 7
btn_5 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="7")
btn_5.pack(pady=20, padx=20)
btn_5.place(x = 21, y = 279)

#button_6 is 8
btn_6 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="8")
btn_6.pack(pady=20, padx=20)
btn_6.place(x = 112, y = 279)

#button_7 is 9
btn_7 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="9")
btn_7.pack(pady=20, padx=20)
btn_7.place(x = 202, y = 279)

#button_8 is /
btn_8 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="/")
btn_8.pack(pady=20, padx=20)
btn_8.place(x = 293, y = 279)

#button_9 is 4
btn_9 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="4")
btn_9.pack(pady=20, padx=20)
btn_9.place(x = 21, y = 355)

#button_10 is 5
btn_10 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="5")
btn_10.pack(pady=20, padx=20)
btn_10.place(x = 112, y = 355)

#button_11 is 6
btn_11 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="6")
btn_11.pack(pady=20, padx=20)
btn_11.place(x = 202, y = 355)

#button_12 is *
btn_12 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="*")
btn_12.pack(pady=20, padx=20)
btn_12.place(x = 293, y = 355)

#button_13 is 1
btn_13 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="1")
btn_13.pack(pady=20, padx=20)
btn_13.place(x = 21, y = 430)

#button_14 is 2
btn_14 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="2")
btn_14.pack(pady=20, padx=20)
btn_14.place(x = 112, y = 430)

#button_15 is 3
btn_15 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="3")
btn_15.pack(pady=20, padx=20)
btn_15.place(x = 202, y = 430)

#button_16 is -
btn_16 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="-")
btn_16.pack(pady=20, padx=20)
btn_16.place(x = 293, y = 430)

#button_17 is 0
btn_17 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="0")
btn_17.pack(pady=20, padx=20)
btn_17.place(x = 21, y = 506)

#button_18 is ,
btn_18 = CTkButton(master=app, width=87, height=63, corner_radius=32, text=",")
btn_18.pack(pady=20, padx=20)
btn_18.place(x = 112, y = 506)

#button_19 is =
btn_19 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="=")
btn_19.pack(pady=20, padx=20)
btn_19.place(x = 202, y = 506)

#button_20 is +
btn_20 = CTkButton(master=app, width=87, height=63, corner_radius=32, text="+")
btn_20.pack(pady=20, padx=20)
btn_20.place(x = 293, y = 506)


#starting the app
app.mainloop()