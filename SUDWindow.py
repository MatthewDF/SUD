from art import *
import tkinter as tk

window = tk.Tk()

# Creates a window to display text to the user and allow the user to input commands


# Take current text in user input field and submit
def input_handler(event=None):
    user_input = entry_field.get()
    entry_field.delete(0, tk.END)

    window_txt_display.insert(tk.END, "\n" + user_input)

    # Send user input to command module to see if their input matches a command

    # A return value will be sent by command module if command is not a match. If that's so, print error msg


# Write output to screen. If text length is too long, wrap it
def output():
    pass


frame_display = tk.Frame(master=window)
frame_display.grid(column=0, row=1)
window_txt_display = tk.Text(master=frame_display, height=30, width=60, bg="black", fg="white")
window_txt_display.pack(fill=tk.BOTH)

frame_text = tk.Frame(master=window)
frame_text.grid(column=0, row=2, sticky="w")
entry_field = tk.Entry(master=frame_text, width=68)
entry_field.pack()

frame_button = tk.Frame(master=window)
frame_button.grid(column=0, row=2, sticky="e")
submit = tk.Button(master=frame_button, text="Submit", command=input_handler, height=2, width=8)
submit.pack(side=tk.RIGHT, fill=tk.BOTH)

entry_field.bind('<Return>', input_handler)

window.mainloop()