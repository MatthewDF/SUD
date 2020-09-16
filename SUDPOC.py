from art import *
import tkinter as tk


#class TextGUI:
# Draws and updates the Tkinter window with user input and game content
window = tk.Tk()

frame = tk.Frame(master=window, bg="black", width=60, height=180)
frame.pack(fill=tk.BOTH, expand=True)

entry_field = tk.Entry(window)
entry_field.pack(fill=tk.X)

window_txt_display = tk.Text(master=frame, height=30, width=60, bg="black", fg="white")
window_txt_display.pack(fill=tk.BOTH)

# Text loading for examples
text_to_print= []
text_intro = text2art(text="SUD POC")
start_prompt = "Hit enter to begin\n"
rambling_intro = "A narrow dirt path stretches forward and down the hill you stand upon, winding its way through a " \
                 "long valley of green grass. In the distance, white snowcapped mountains beckon you."


def input_handler(event=None):
    # Takes user input from the entry field and compares it to execute
    user_input = entry_field.get()

    entry_field.delete(0, tk.END)

    if user_input == "load":
        window_txt_display.insert(tk.END, "\n\n" + text_intro)
        window_txt_display.insert(tk.END, "\n\n" + start_prompt)

        # text_to_print.append(text_intro)
        # text_to_print.append(start_prompt)

    if user_input == "":
        window_txt_display.insert(tk.END, "\n\n" + rambling_intro)
        # text_to_print.append(rambling_intro)

    #for indx, item in enumerate(text_to_print):
        # text_to_print.pop(indx)
        # print(text_to_print)
        # text_display.insert(2.0, "\n" + item)


entry_field.bind("<Return>",input_handler)

window.mainloop()


# class InputCommands:
#     #Compares user input from TextGUI with commands, then executes code depending on command
#     None

