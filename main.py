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


# ---------------------------- TIMER RESET ------------------------------- # 



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(WORK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min= math.floor(count/60)
    count_sec= count % 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count -1)


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
                      font=(FONT_NAME, 14, "bold"))
reset_button.grid(column=2, row=2)

TEXT= "\u2713"
check_mark =Label(text=TEXT, font=(FONT_NAME, 14, "bold"), fg=GREEN, bg= YELLOW)
check_mark.grid(column=1, row=3)






window.iconphoto(False, pomodoro_img)
window.mainloop()