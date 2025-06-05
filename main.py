import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

# Set up main window
root = tk.Tk()
root.title("Dice Roller")
root.geometry("300x300")
root.configure(bg="#1e1e1e")

# Define style for ttk Button
style = ttk.Style()
style.theme_use('clam')  # Use a theme that allows styling
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

# Load dice images
dice_images = []
for i in range(1, 5):
    img = Image.open(f"dice{i}.png").resize((100, 100))
    dice_images.append(ImageTk.PhotoImage(img))

# Roll logic
def roll_dice():
    result = random.randint(0, len(dice_images) - 1)
    dice_label.config(image=dice_images[result])
    dice_label.image = dice_images[result]
    result_label.config(text=f"You rolled a {result + 1}!")

# Dice display
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

# Roll button (styled)
roll_button = ttk.Button(
    root,
    text="🎲 Roll Dice",
    style="Custom.TButton",
    command=roll_dice
)
roll_button.pack(pady=10)

# Initial roll
roll_dice()
root.mainloop()

