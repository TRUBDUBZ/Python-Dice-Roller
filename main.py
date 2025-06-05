import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import os

# Color scheme
ACCENT_COLOR = "#d2fa52"  # Bright lime green
DARK_COLOR = "#3f4139"    # Dark gray-green
LIGHT_COLOR = "#f4f3ef"   # Light off-white

# Set up main window
root = tk.Tk()
root.title("Dice Roller")
root.minsize(400, 400)  # Set minimum window size
root.configure(bg=DARK_COLOR)

# Make the window resizable
root.resizable(True, True)

# Configure grid weights to make the layout responsive
for i in range(6):  # Added one more row for dice counter
    root.grid_rowconfigure(i, weight=1)
root.grid_columnconfigure(0, weight=1)

# Define style for ttk Button and Frame
style = ttk.Style()
style.theme_use('clam')  # Use a theme that allows styling
style.configure(
    "Custom.TButton",
    background=ACCENT_COLOR,
    foreground=DARK_COLOR,
    font=("Helvetica", 16, "bold"),
    padding=10,
)
style.map(
    "Custom.TButton",
    background=[("active", "#b8e04a")],  # Slightly darker shade of accent color
    foreground=[("active", DARK_COLOR)]
)

# Configure ttk Frame style
style.configure("TFrame", background=DARK_COLOR)

# Configure modern spinbox style
style.configure(
    "Modern.TSpinbox",
    fieldbackground=DARK_COLOR,
    background=DARK_COLOR,
    foreground=LIGHT_COLOR,
    arrowcolor=ACCENT_COLOR,
    bordercolor=ACCENT_COLOR,
    lightcolor=ACCENT_COLOR,
    darkcolor=ACCENT_COLOR,
    font=("Helvetica", 12)
)
style.map(
    "Modern.TSpinbox",
    fieldbackground=[("readonly", DARK_COLOR)],
    selectbackground=[("readonly", ACCENT_COLOR)],
    selectforeground=[("readonly", DARK_COLOR)]
)

# Load dice images
dice_images = []
for i in range(1, 7):  # Changed to load dice 1 through 6
    img = Image.open(f"dice{i}.png")
    # Make the image size relative to the window size
    img = img.resize((150, 150), Image.Resampling.LANCZOS)
    dice_images.append(ImageTk.PhotoImage(img))

# Create a frame to hold all widgets with padding
main_frame = ttk.Frame(root, style="TFrame")
main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

# Configure main frame grid
for i in range(6):
    main_frame.grid_rowconfigure(i, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# Add some spacing at the top
spacer_top = ttk.Frame(main_frame, style="TFrame", height=20)
spacer_top.grid(row=0, column=0, sticky="ew")

# Create counter frame
counter_frame = ttk.Frame(main_frame, style="TFrame")
counter_frame.grid(row=1, column=0, sticky="nsew", pady=10)

# Create a frame to hold the counter elements
counter_elements_frame = ttk.Frame(counter_frame, style="TFrame")
counter_elements_frame.grid(row=0, column=0, sticky="nsew")

# Add a subtle border around the counter
counter_border = ttk.Frame(
    counter_elements_frame,
    style="TFrame",
    relief="solid",
    borderwidth=1
)
counter_border.pack(fill="both", expand=True, padx=5, pady=5)

# Create an inner frame for the counter elements
counter_inner_frame = ttk.Frame(counter_border, style="TFrame")
counter_inner_frame.pack(fill="both", expand=True, padx=10, pady=5)

# Number of dice label
dice_count_label = tk.Label(
    counter_inner_frame,
    text="Number of Dice:",
    font=("Helvetica", 12),
    bg=DARK_COLOR,
    fg=LIGHT_COLOR
)
dice_count_label.pack(side=tk.LEFT, padx=(0, 10))

# Number of dice counter
dice_count = tk.IntVar(value=1)
dice_count_spinbox = ttk.Spinbox(
    counter_inner_frame,
    from_=1,
    to=10,
    textvariable=dice_count,
    width=5,
    font=("Helvetica", 12),
    style="Modern.TSpinbox",
    wrap=True  # Enable wrapping from max to min value
)
dice_count_spinbox.pack(side=tk.LEFT, padx=5)

# Dice display frame
dice_frame = ttk.Frame(main_frame, style="TFrame")
dice_frame.grid(row=2, column=0, sticky="nsew", pady=10)

# Configure dice frame to center its contents
dice_frame.grid_columnconfigure(0, weight=1)
dice_frame.grid_columnconfigure(2, weight=1)

# List to store dice labels
dice_labels = []

# Result label
result_label = tk.Label(
    main_frame,
    text="",
    font=("Helvetica", 16),
    bg=DARK_COLOR,
    fg=LIGHT_COLOR
)
result_label.grid(row=3, column=0, sticky="nsew", pady=10)

# Sum label
sum_label = tk.Label(
    main_frame,
    text="",
    font=("Helvetica", 16, "bold"),
    bg=DARK_COLOR,
    fg=ACCENT_COLOR  # Using accent color for the sum to make it stand out
)
sum_label.grid(row=4, column=0, sticky="nsew", pady=5)

# Roll logic
def roll_dice():
    # Clear previous dice
    for label in dice_labels:
        label.destroy()
    dice_labels.clear()
    
    # Get number of dice to roll
    num_dice = dice_count.get()
    results = []
    
    # Create a frame to hold the dice in a row
    dice_row_frame = ttk.Frame(dice_frame, style="TFrame")
    dice_row_frame.grid(row=0, column=1, sticky="nsew")
    
    # Roll the dice
    for i in range(num_dice):
        result = random.randint(0, len(dice_images) - 1)
        results.append(result + 1)
        
        # Create and display dice image
        dice_label = tk.Label(dice_row_frame, bg=DARK_COLOR)
        dice_label.pack(side=tk.LEFT, padx=5)
        dice_label.config(image=dice_images[result])
        dice_label.image = dice_images[result]
        dice_labels.append(dice_label)
    
    # Update result text
    if num_dice == 1:
        result_label.config(text=f"You rolled a {results[0]}!")
        sum_label.config(text="")
    else:
        result_label.config(text=f"You rolled: {', '.join(map(str, results))}")
        sum_label.config(text=f"Sum: {sum(results)}")

# Clear button
def clear_dice():
    # Destroy any dice labels
    for label in dice_labels:
        label.destroy()
    dice_labels.clear()

    # Clear the result and sum labels
    result_label.config(text="")
    sum_label.config(text="")

# Roll button (styled)
roll_button = ttk.Button(
    main_frame,
    text="🎲 Roll Dice",
    style="Custom.TButton",
    command=roll_dice
)
roll_button.grid(row=5, column=0, sticky="nsew", pady=10)

clear_button = ttk.Button(
    main_frame,
    text="🧹 Clear",
    style="Custom.TButton",
    command=clear_dice
)
clear_button.grid(row=6, column=0, sticky="nsew", pady=(0, 20))

# Function to handle window resize
def on_window_resize(event):
    # Only handle main window resize events
    if event.widget != root:
        return
        
    # Calculate new size with safety checks
    new_size = max(50, min(event.width, event.height) // 4)  # Reduced size to accommodate multiple dice
    
    try:
        # Update dice image sizes based on new window size
        for i in range(len(dice_images)):
            img = Image.open(f"dice{i+1}.png")
            img = img.resize((new_size, new_size), Image.Resampling.LANCZOS)
            dice_images[i] = ImageTk.PhotoImage(img)
        
        # Update current dice display if there are any
        if dice_labels:
            # Get the current results from the result label
            result_text = result_label.cget("text")
            if "rolled: " in result_text:
                # Multiple dice case
                results = [int(x) for x in result_text.split("rolled: ")[1].split("!")[0].split(", ")]
            else:
                # Single die case
                results = [int(result_text.split("rolled a ")[1].split("!")[0])]
            
            # Update each dice label with the new size
            for i, result in enumerate(results):
                if i < len(dice_labels):
                    dice_labels[i].config(image=dice_images[result - 1])
                    dice_labels[i].image = dice_images[result - 1]
    except Exception as e:
        print(f"Error during resize: {e}")

# Bind resize event
root.bind("<Configure>", on_window_resize)

# Initial roll
roll_dice()
root.mainloop()
