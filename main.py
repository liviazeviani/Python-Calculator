from tkinter import *
from tkinter import ttk


color1 = "#b5b3b4"
color2 = "#999798"
color3 ="#f26d83"
color4 ="#dae0db"
color5 ="#ebaf6e"
color6 ="#f0e6dd"

font1 = 'Ivy 10 bold'
font2 = 'Ivy 8 bold'
font3 = 'Ivy 18'

window =Tk()
window.title("Calculator")
window.geometry("250x300")
window.config(bg=color1)

frame_screen = Frame(window, width=230, height=50, bg=color1)
frame_screen.grid(row=0, column=0, pady=4)

frame_body = Frame(window, width=250, height=270, bg=color2)
frame_body.grid(row=1, column=0)

values = ''
def input_value(x):

    global values
    values = values + str(x)
    text_value.set(values)

def calculate():
    global values
    result =eval(values)

    text_value.set(str(result))


def clean():
    global values
    values =''
    text_value.set('')

text_value = StringVar()
app_label = Label(frame_screen, textvariable=text_value, width=8, height=1, font=font3, padx=2, anchor="e", justify=RIGHT, bg=color1)
app_label.place(x=100, y=0)

b_1 = Button(frame_body, command=clean, text="Clean", width=8, height=1, fg=color6, bg=color3, font=font1)
b_1.place(x=10, y=8.5)
b_2 = Button(frame_body,
             text="%",
             width=3,
             height=2,
             bg=color4,
             font=font2,
             command=lambda: input_value('%'))
b_2.place(x=125, y=4.9)
b_3 = Button(frame_body,
             text="/",
             width=3,
             height=2,
             bg=color5,
             font=font2,
             command=lambda: input_value('/'))
b_3.place(x=185, y=4.9)

b_4 = Button(frame_body, text="7", width=3, height=2, bg=color4, font=font2, command=lambda: input_value('7'))
b_4.place(x=10, y=50)
b_5 = Button(frame_body, text="8", width=3, height=2, bg=color4, font=font2, command=lambda: input_value('8'))
b_5.place(x=67, y=50)
b_6 = Button(frame_body, text="9", width=3, height=2, bg=color4, font=font2, command=lambda: input_value('9'))
b_6.place(x=125, y=50)
b_7 = Button(frame_body, text="*", width=3, height=2, bg=color5, font=font2, command=lambda: input_value('*'))
b_7.place(x=185, y=50)

b_8 = Button(frame_body, text="4", width=3, height=2, bg=color4, font=font2, command=lambda: input_value('4'))
b_8.place(x=10, y=100)
b_9 = Button(frame_body, text="5", width=3, height=2, bg=color4, font=font2, command=lambda: input_value('5'))
b_9.place(x=67, y=100)
b_10 = Button(frame_body, text="6", width=3, height=2, bg=color4, font=font2, command=lambda: input_value('6'))
b_10.place(x=125, y=100)
b_11 = Button(frame_body, text="-", width=3, height=2, bg=color5, font=font2, command=lambda: input_value('-'))
b_11.place(x=185, y=100)

b_12 = Button(frame_body, text="1", width=3, height=2, bg=color4, font=font2, command=lambda: input_value('1'))
b_12.place(x=10, y=150)
b_13 = Button(frame_body, text="2", width=3, height=2, bg=color4, font=font2, command=lambda: input_value('2'))
b_13.place(x=67, y=150)
b_14 = Button(frame_body, text="3", width=3, height=2, bg=color4, font=font2, command=lambda: input_value('3'))
b_14.place(x=125, y=150)
b_15 = Button(frame_body, text="+", width=3, height=2, bg=color5, font=font2, command=lambda: input_value('+'))
b_15.place(x=185, y=150)

b_16 = Button(frame_body, text="0", width=10, height=2, bg=color4, font=font2, command=lambda: input_value('0'))
b_16.place(x=10, y=200)
b_17 = Button(frame_body, text=".", width=3, height=2, bg=color4, font=font2, command=lambda: input_value('.'))
b_17.place(x=125, y=200)
b_18 = Button(frame_body, text="=", width=3, height=2, bg=color5, font=font2, command=calculate)
b_18.place(x=185, y=200)


window.mainloop()


