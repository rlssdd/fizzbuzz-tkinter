import tkinter.font
from tkinter import *


def fizzbuzz():
    txt.delete("1.0", "end")
    try:
        number = int(entry.get())
        for number in range(1, number + 1):
            if number % 3 == 0 and number % 5 == 0:
                txt.insert(END, f" FIZZBUZZ({number})")
                continue
            elif number % 3 == 0:
                txt.insert(END, f" FIZZ({number}) ")
                continue
            elif number % 5 == 0:
                txt.insert(END, f" BUZZ({number}) ")
                continue
            txt.insert(END, " " + str(number))
    except:
        txt.insert(END, "ENTER A VALID NUMBER")


window = Tk()
my_string_var = StringVar()
window.title("FizzBuzz by Arel")
window.config(padx=100, pady=50)
fontStyle = tkinter.font.Font(family="Lucida Grande", size=20)
canvasOne = Canvas(width=400, height=400, highlightthickness=0)
button = Button(text="FizzBuzz Me", command=fizzbuzz)
txt = Text(window, height=5, width=95)

label = Label(text="FizzBuzz", font=fontStyle)
entry = Entry(bg="red", fg="yellow", font="David 26", justify="center")

canvasOne.create_window(200, 250, window=entry)
canvasOne.create_window(200, 300, window=button)
filename = PhotoImage(file="boom.png")
image = canvasOne.create_image(210, 160, image=filename)

label.pack()
canvasOne.pack()
txt.pack()
window.mainloop()
