from tkinter import *
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
timer_count = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_count)
    timer.config(text="Timer")
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        timer.config(text="Break", fg=RED)
    elif reps % 2 == 1:
        count_down(WORK_MIN*60)
        timer.config(text="Work")
    else:
        count_down(SHORT_BREAK_MIN*60)
        timer.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_count
        timer_count = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps//2):
            mark += "√"
            check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# load = Image.open("tomato.png")
# img = ImageTk.PhotoImage(load)
# canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer.grid(row=0, column=1)

start_button = Button(text="Start", width=10, height=5, highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", width=10, height=5, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

window.mainloop()