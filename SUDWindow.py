from art import *
import tkinter as tk

window = tk.Tk()

# Create a window that will receive text from the rest of the program and display it for the user. Get width of window
# and if the text is too wide, wrap it.

# Window drawing
frame_display = tk.Frame(master=window, bg="black", height=30, width=60)
frame_display.grid(column=0, row=1)
window_txt_display = tk.Text(master=frame_display, height=30, width=60, bg="black", fg="white")
window_txt_display.pack(fill=tk.BOTH)

frame_text = tk.Frame(master=window, height=50, width=20)
frame_text.grid(column=0, row=2, sticky="w")
entry_field = tk.Entry(master=frame_text, width=68)
entry_field.pack(padx=2, pady=2)

frame_button = tk.Frame(master=window)
frame_button.grid(column=0, row=2, sticky="e")
submit = tk.Button(master=frame_button, text="Submit", height=2, width=8)
submit.pack(side=tk.RIGHT, fill=tk.BOTH)

window.mainloop()

# Draw submit button

