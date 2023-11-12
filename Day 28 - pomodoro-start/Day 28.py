from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", foreground=GREEN)
    meter.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    if reps % 2 != 0:
        countdown(WORK_MIN * 60)
        title.config(text="Work Time", foreground=RED)
    elif reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        title.config(text="Long Break", foreground= GREEN)
    else:
        countdown(SHORT_BREAK_MIN * 60)
        title.config(text="Short Break", foreground=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        check_mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check_mark += "✓"
        meter.config(text= check_mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
tomato_img = PhotoImage(file="tomato.png")
window.config(padx=100, pady=60, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=("Courier", 24, "bold"), fill="White")
canvas.grid(column=1, row=1)

# Title
title = Label(text="Timer", font=("Courier", 30, "bold"), foreground=GREEN, bg=YELLOW)
title.grid(column=1, row=0)

# Start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Pomodoro meter
meter = Label(foreground=GREEN, bg=YELLOW)
meter.grid(column=1, row=3)

window.mainloop()