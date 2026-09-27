import tkinter as tk
import time
import random

root = tk.Tk()
root.title("Typing Tester")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

task_bar_height = 50
window_height = screen_height - task_bar_height

root.geometry(f"{screen_width}x{window_height}+0+0")

sample_texts = [
    "The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet and is commonly used for typing practice tests to measure speed and accuracy.",
    "Programming is the process of creating a set of instructions that tell a computer how to perform a task.",
    "Python is a high-level programming language known for its simplicity and readability.",
    "Artificial intelligence is transforming the way we interact with technology.",
    "Machine learning algorithms can learn from data without being explicitly programmed.",
    "Web development involves creating websites and web applications that run on the internet.",
    "There a many programming languages in the world! Many have different uses and functions. Programming is very diverse!",
    "Oh no! A cat ran over my keyboard! cat fat rat mat pat sat chat. Sorry for the inconvenience!"
]

sample_text = ""

start_time = 0
test_running = False

def start_test():
    global start_time, test_running, sample_text
    test_running = True
    start_time = time.time()
    sample_text = random.choice(sample_texts)  # Pick new sentence each round
    text_display.config(text=sample_text)  # Update the display
    start_button.config(state="disabled")
    text_input.config(state="normal")
    text_input.delete(0, tk.END)
    text_input.focus()
    instructions.config(text="Start typing!")

def end_test(event=None):
    global test_running
    if not test_running:
        return

    test_running = False
    end_time = time.time()
    time_taken = end_time - start_time

    typed_text = text_input.get()

    # Calculate accuracy
    correct_chars = 0
    for i in range(min(len(typed_text), len(sample_text))):
        if typed_text[i] == sample_text[i]:
            correct_chars += 1

    accuracy = (correct_chars / len(sample_text)) * 100 if len(sample_text) > 0 else 0

    # Calculate WPM (words per minute)
    # Standard: 5 characters = 1 word
    characters_typed = len(typed_text)
    wpm = (characters_typed / 5) / (time_taken / 60) if time_taken > 0 else 0

    instructions.config(text=f"Time: {time_taken:.2f}s | WPM: {wpm:.1f} | Accuracy: {accuracy:.1f}%")
    start_button.config(state="normal")
    start_button.config(text="Try Again")
    text_input.config(state="disabled")

title = tk.Label(root, text="TYPING TESTER", font=("Arial", 40))
title.pack(pady=20)

instructions = tk.Label(root, text="Press Start to begin typing!", font=("Arial", 20))
instructions.pack(pady=10)

text_display = tk.Label(root, text=sample_text, font=("Arial", 16), wraplength=screen_width-100)
text_display.pack(pady=20)

text_input = tk.Entry(root, font=("Arial", 16), state="disabled")
text_input.pack(pady=20, padx=50)
text_input.bind("<Return>", end_test)

start_button = tk.Button(root, text="Start", font=("Arial", 20), height=2, width=10, command=start_test)
start_button.pack(pady=20)

root.mainloop()
