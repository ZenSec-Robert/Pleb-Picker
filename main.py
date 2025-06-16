import tkinter as tk
import random
from data import legends, weapons
from PIL import Image, ImageTk

#Colors
bg_color = "#2b2d42"
text_color = "#edf2f4"
accent_color = "#ef233c"
button_color = "#8d99ae"
button_hover = "#d90429"

#main window
root = tk.Tk()
root.title("🌸 Pleb Picker: Apex Loadout Generator 🌸")
root.geometry("650x400")
root.configure(background=bg_color)

# Load and resize the background image
bg_image = Image.open("image.jpg")
bg_image = bg_image.resize((650, 400), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Place the image in the background
background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#dynamic text display
result_text = tk.StringVar()
result_text.set("Click below to reveal your fate ✨")

result_label = tk.Label(
    root,
    textvariable=result_text,
    font=("Segoe UI", 17),
    wraplength=420,
    justify="center",
    background=bg_color,
    fg=text_color
)
result_label.pack(pady=(80, 20))

#Loadout generator function
def generate_loadout():
    legend = random.choice(legends)
    guns = random.sample(weapons, 2)
    result_text.set(f"🎮 Legend: {legend}\n🔫 Guns: {guns[0]} and {guns[1]}\n🌸 Good luck!")

#button with hover effect
def on_enter(e):
    generate_button['background'] = button_hover

def on_leave(e):
    generate_button['background'] = button_color

generate_button = tk.Button(
    root,
    text="✨ Give me a loadout ✨",
    command=generate_loadout,
    font=("Segoe UI", 18),
    background=button_color,
    fg="white",
    activeforeground="white",
    activebackground=button_hover,
    borderwidth=0,
    padx=12,
    pady=6
)
generate_button.pack(pady=(0, 20))

generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)

root.mainloop()
