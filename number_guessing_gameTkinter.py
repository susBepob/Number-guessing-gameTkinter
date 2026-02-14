import tkinter as tk
import random

# ----- Game state -----
random_number = None
count = 0
game_running = False

# ----- Functions -----
def start_game():
    global random_number, count, game_running
    random_number = random.randrange(101)
    count = 1
    game_running = True
    result_label.config(text="Game started! Guess a number 0 - 100")
    attempt_label.config(text="Attempt: 1")
    entry.delete(0, tk.END)
    entry.focus()

def make_guess():
    global count, game_running

    if not game_running:
        result_label.config(text="Press Start first!")
        return

    try:
        guess = int(entry.get())

        if guess < 0 or guess > 100:
            result_label.config(text="Only numbers 0 - 100 allowed")
            return

        if guess == random_number:
            result_label.config(
                text=f"Correct!! You guessed it in {count} attempts!"
            )
            game_running = False
            return

        elif guess < random_number:
            result_label.config(text="Go higher")

        else:
            result_label.config(text="Go lower")

        count += 1
        attempt_label.config(text=f"Attempt: {count}")
        entry.delete(0, tk.END)

    except ValueError:
        result_label.config(text="Enter a valid integer")

def quit_game():
    window.destroy()

# ----- Window -----
window = tk.Tk()
window.title("Guess The Number")
window.geometry("350x250")

title = tk.Label(window, text="Guess the Number", font=("Arial", 16))
title.pack(pady=10)

result_label = tk.Label(window, text="Press Start to play")
result_label.pack(pady=10)

attempt_label = tk.Label(window, text="Attempt: 0")
attempt_label.pack()

entry = tk.Entry(window, justify="center")
entry.pack(pady=10)

guess_btn = tk.Button(window, text="Guess", command=make_guess)
guess_btn.pack(pady=5)

start_btn = tk.Button(window, text="Start", command=start_game)
start_btn.pack(pady=5)

quit_btn = tk.Button(window, text="Quit", command=quit_game)
quit_btn.pack(pady=5)

window.mainloop()