from art import *
import tkinter as tk

window = tk.Tk()

# Create a window that will receive text from the rest of the program and display it for the user. Get width of window
# and if the text is too wide, wrap it.

# Window drawing
frame = tk.Frame(master=window, bg="black", height=30, width=60)
frame.pack(fill=tk.BOTH, expand=True)

entry_field = tk.Entry(window)
entry_field.pack(fill=tk.X)

window_txt_display = tk.Text(master=frame, height=30, width=60, bg="black", fg="white")
window_txt_display.pack(fill=tk.BOTH)

submit = tk.Button(master=entry_field, text="Submit", height=2, width=8)
submit.pack(side=tk.RIGHT)

window.mainloop()

# Draw submit button

