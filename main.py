import tkinter as tk
from tkinter import *
from tkinter import messagebox
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
MIN = 60
timer = None
user_words = []


with open("text.txt") as my_file:
    data = my_file.read()
    text = data.split(" ")

def user_type(event):
    user_words.append(entry.get().strip())
    entry.delete(0, "end")

##Test test function
def result():
    global text
    correct = 0
    total = 0
    global user_words
    for i in user_words:
        if i in text:
            correct += 1
        else:
            correct = correct
        total += 1

    messagebox.showinfo(title="Result", message=f'TOTAL WORDS: {total}\nCORRECT WORDS: {correct}')


def start_time(event):
    min = MIN
    count_down(min)
    window.unbind("<Return>")

def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
       result()

def reset_time():
    ##stop start_timer()
    global timer
    global user_words
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="01:00")
    user_words = []
    window.bind("<Return>", start_time)


window = Tk()
window.title("Checking your typing speed")
window.config(height=600, width=600, padx=100, pady=50)

##Text Image

##Create Canvas
canvas = Canvas(width=700, height=300, bg=YELLOW, highlightthickness=0)
canvas.create_text(350,50, text= "users canvas longitude short ask green point short plan miss dry\n"
                                   "far though went still sky look horse just those start begin done\n"
                                   "fire dog build play long to enough some any more number python code\n"
                                   "draw bed soon cry under pull force student teacher family member\n"
                                   "car long tall rain summer snow word difficult but unfair speed lack", font=(FONT_NAME, 12, "bold"))
timer_text= canvas.create_text(200, 150, text="01:00", fill="black", font=(FONT_NAME, 15, "bold"))
canvas.grid(column=1, row=0, columnspan=3, rowspan=2)
canvas.create_text(350,200, text="Please press RETURN to start", font=(FONT_NAME, 12, "bold"))
canvas.grid(column=1, row= 2)

entry = Entry(width=50, font=(FONT_NAME, 12, "bold"))
entry.grid(column=1, row=4)
window.bind("<Return>", start_time)
window.bind("<space>", user_type)
##Reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_time)
reset_button.grid(column=2, row=5)





window.mainloop()