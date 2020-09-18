from art import *
import tkinter as tk

window = tk.Tk()

# Create a window that will receive text from the rest of the program and display it for the user. Get width of window
# and if the text is too wide, wrap it.

# Window drawing
frame = tk.Frame(master=window, bg="black", height=30, width=60)
frame.pack(fill=tk.BOTH, expand=True)

window_txt_display = tk.Text(master=frame, height=30, width=60, bg="black", fg="white")
window_txt_display.pack(fill=tk.BOTH)

entry_field = tk.Entry(master=window)
entry_field.pack(fill=tk.X)

submit = tk.Button(master=window, text="Submit", height=2, width=8)
submit.pack(side=tk.RIGHT, fill=tk.BOTH)

window.mainloop()

# Draw submit button

