from tkinter import *
import math
import pygame

# ---------------------------- CONSTANTS ------------------------------- #
# Define color constants for use in the UI
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30

# Global variables
rep = 0  # Number of repetitions (work and break cycles)
time = None  # Variable to keep track of the timer

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    """Reset the timer and the repetition counter."""
    global rep
    screen.after_cancel(time)  # Cancel any ongoing timer
    timer_lable.config(text="Timer")  # Reset the label text
    canvas.itemconfig(timer, text="00:00")  # Reset the timer display
    rep = 0  # Reset the repetition count

# ---------------------------- TIMER MECHANISM ------------------------------- #
def play_sound(sound_file):
    """Play a sound file."""
    pygame.mixer.init()  # Initialize the mixer module
    pygame.mixer.music.load(sound_file)  # Load the sound file
    pygame.mixer.music.play()  # Play the sound

def start():
    """Start the timer and handle work/break cycles."""
    global rep
    rep += 1  # Increment the repetition count
    work = WORK_MIN * 60  # Convert work time from minutes to seconds
    short_rest = SHORT_BREAK_MIN * 60  # Convert short break time from minutes to seconds
    long_rest = LONG_BREAK_MIN * 60  # Convert long break time from minutes to seconds

    # Determine which timer to start based on the repetition count
    if rep == 8:
        count_down(long_rest)  # Long break after 8 cycles
        timer_lable.config(text="Break", fg=YELLOW)  # Update label for long break
        play_sound("Enjoy your long break 1.wav")  # Play long break sound
    elif rep % 2 != 0 and rep < 8:
        count_down(work)  # Work period
        timer_lable.config(text="Work", fg=RED)  # Update label for work
        play_sound("Its time to work 1.wav")  # Play work sound
    elif rep % 2 == 0 and rep < 8:
        count_down(short_rest)  # Short break period
        timer_lable.config(text="Break", fg=PINK)  # Update label for short break
        play_sound("Take a short break 1.wav")  # Play short break sound
        screen.wm_deiconify()  # Ensure the window is visible
        screen.attributes('-topmost', 1)  # Bring the window to the front

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(second):
    """Count down from a given number of seconds and update the timer display."""
    global rep, time
    min = math.floor(second / 60)  # Calculate minutes
    sec = second % 60  # Calculate seconds
    if min < 10:
        min = f"0{min}"  # Format minutes
    if sec < 10:
        sec = f"0{sec}"  # Format seconds
    canvas.itemconfig(timer, text=f"{min}:{sec}")  # Update timer display
    if second > 0:
        time = screen.after(1000, count_down, second - 1)  # Update the countdown every second
    else:
        screen.attributes('-topmost', 0)  # Remove the topmost attribute
        start()  # Start the next timer period
        tik_text = "✓" * math.floor(rep / 2)  # Update checkmark display
        checkmark_lable.config(text=tik_text)  # Show completed cycles

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomodoro Timer")  # Set window title
screen.config(bg=YELLOW, padx=100, pady=50)  # Configure window background color and padding

# Load and display the tomato image
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=210, height=233, background=YELLOW, highlightthickness=0)
canvas.create_image(105, 116.5, image=tomato_img)
timer = canvas.create_text(115, 130, text="00:00", fill="white", font=(FONT_NAME, 33, "italic", "bold"))
canvas.grid(column=1, row=1)

# Create and configure the timer label
timer_lable = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_lable.grid(column=1, row=0)

# Create and configure buttons for starting and resetting the timer
start_button = Button(text="Start", highlightthickness=0, command=start)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

# Create and configure label for checkmarks
checkmark_lable = Label(fg=GREEN, bg=YELLOW)
checkmark_lable.grid(column=1, row=2)

screen.mainloop()  # Start the Tkinter event loop
