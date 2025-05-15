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
    global timer
    if timer is not None:
        window.after_cancel(timer)
        timer = None

    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW,
                        font=(FONT_NAME, 50, "bold"))
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec =LONG_BREAK_MIN * 60

    if reps%8 == 0:
        timer_label.config(text="Long break", fg=RED)
        count_down(int(long_break_sec))
    elif reps%2 == 0:

        timer_label.config(text="Break", fg=PINK)
        count_down(int(short_break_sec))

    else:
        timer_label.config(text="WORK", fg=GREEN)
        count_down(int(work_sec))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min= math.floor(count/60)
    count_sec= int(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        check_mark_symbol = "\u2713"
        work_session = math.floor(reps/2)

        for _ in range(work_session):
            marks+= check_mark_symbol
        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=20, pady=20, bg=YELLOW)





canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=pomodoro_img)
timer_text= canvas.create_text(100,130, text="00:00", fill="white",
                               font=(FONT_NAME,34,"bold"))
canvas.grid(column=1, row=1)


window.update_idletasks()
w = window.winfo_width()
h = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (w // 2)
y = (window.winfo_screenheight() // 2) - (h // 2)
window.geometry(f'+{x}+{y}')


timer_label = Label(text="Timer", fg=GREEN,bg=YELLOW,
                    font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)


start_button = Button(text="Start", highlightthickness=0,
                      font=(FONT_NAME, 14, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0,
                      font=(FONT_NAME, 14, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark =Label(font=(FONT_NAME, 14, "bold"), fg=GREEN, bg= YELLOW)
check_mark.grid(column=1, row=3)






window.iconphoto(False, pomodoro_img)
window.mainloop()