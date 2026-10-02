import customtkinter as ctk

import random

root = ctk.CTk()

root.title("Hit The Button Game")

# Dark mode
ctk.set_appearance_mode("dark")

# Get screen dimensions

screen_width = root.winfo_screenwidth()

screen_height = root.winfo_screenheight()

# Subtract task bar space

task_bar_height = 50

window_height = screen_height - task_bar_height

# Set geometry to full screen minus task bar

root.geometry(f"{screen_width}x{window_height}+0+0")

click_count = 0

timer = 60

game_active = False  # Start with game inactive


def update_timer():

    global timer, game_active

    if timer > 0 and game_active:

        timer -= 1

        timer_label.configure(text=f"Time: {timer}")

        root.after(1000, update_timer)  # Update every 1 second

    elif timer == 0:

        game_active = False

        button.configure(state="disabled")  # Disable button when time's up

        label.configure(text=f"Game Over!\nFinal Score: {click_count}")


def start_game():

    global game_active, click_count, timer

    game_active = True

    click_count = 0

    timer = 60

    start_button.destroy()

    button.configure(state="normal")  # Enable game button

    label.configure(text="CLICK ME AS FAST AS YOU CAN!!!")

    timer_label.configure(text=f"Time: {timer}")

    update_timer()  # Start the timer


def change_label():

    global click_count

    if game_active:

        # Random position within window bounds (subtracting button size)

        random_x = random.randint(0, screen_width - 100)

        random_y = random.randint(0, window_height - 50)

        button.place(x=random_x, y=random_y)

        click_count += 1

        label.configure(text=f"Score: {click_count}")


label = ctk.CTkLabel(
    root,
    text="Press Start to Begin!",
    font=("Arial", 20)
)

label.pack(pady=20)


start_button = ctk.CTkButton(
    root,
    text="START!",
    command=start_game
)

start_button.pack(pady=10)


timer_label = ctk.CTkLabel(
    root,
    text=f"Time: {timer}",
    font=("Arial", 20)
)

timer_label.pack(pady=20)


button = ctk.CTkButton(
    root,
    text="Click me!",
    command=change_label,
    state="disabled"
)

button.pack()


root.mainloop()
