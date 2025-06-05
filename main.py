import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import os
print("Current working directory:", os.getcwd())
print("Files in this directory:")
print(os.listdir())

# Initialize the window
root = tk.Tk()
root.title("Dice Roller")
root.geometry("300x320")
root.configure(bg="#1e1e1e")

# Configure button style
style = ttk.Style()
style.theme_use('clam')
style.configure(
    "Custom.TButton",
    background="#007acc",
    foreground="#ffffff",
    font=("Helvetica", 16, "bold"),
    padding=10,
)
style.map(
    "Custom.TButton",
    background=[("active", "#005f99")],
    foreground=[("active", "#ffffff")]
)

# Load dice images (1 to 6)
dice_images = []
for i in range(1, 7):
    img = Image.open(f"dice{i}.png").resize((100, 100))
    dice_images.append(ImageTk.PhotoImage(img))

# Dice roll function
def roll_dice():
    result = random.randint(0, 5)  # 0 to 5 for 6 images
    dice_label.config(image=dice_images[result])
    dice_label.image = dice_images[result]
    result_label.config(text=f"You rolled a {result + 1}!")

# Dice image label
dice_label = tk.Label(root, bg="#1e1e1e")
dice_label.pack(pady=20)

# Result label
result_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 16),
    bg="#1e1e1e",
    fg="#f0f0f0"
)
result_label.pack()

# Roll button
roll_button = ttk.Button(
    root,
    text="🎲 Roll Dice",
    style="Custom.TButton",
    command=roll_dice
)
roll_button.pack(pady=10)

# Show initial die
roll_dice()

root.mainloop()
