import tkinter as tk
from tkinter import ttk
import subprocess


# ------> Functions <----------
def change_brightness(value1):

    global selected_item
    selected_item = combobox.get()
    value = float(value1) /100   
    value = round((value+0.50),2)
    print(value)
    brightness = value
    subprocess.run(['xrandr', '--output', selected_item, '--brightness', str(brightness)])


def collecting():
    monitors = []
    # Run the command and capture its output
    command_output = subprocess.check_output(["xrandr", "--listactivemonitors"], universal_newlines=True)

    # Split the output into individual lines
    output_lines = command_output.strip().split('\n')

    # Split each line by spaces and print the last element
    for line in output_lines:
        split_line = line.split()
        if split_line:  # Check if split_line is not empty
            last_element = split_line[-1]  # Get the last element
            print(last_element)
            monitors.append(last_element)
    return monitors

def on_select(event):
    selected_item = combobox.get()
    
def show_popup():
    messagebox.showinfo("Popup", "Easy solving some brigthness Monitor processing in Linux based systems ")


# ------> Tkinter <----------


root = tk.Tk()
root.title("Brigthnessizer")
root.geometry("600x100")  # Set window size
root.resizable(False, False)

monitors = collecting()

#global monitors[]
global selected_item
# Create label for "Adapters" at the top left
adapters_label = ttk.Label(root, text="Monitors")
adapters_label.grid(row=0, column=0, padx=40, pady=0, sticky="w")

# Create a frame
frame = ttk.Frame(root)
frame.grid(row=1, column=0, padx=40, pady=0, sticky="w")

# Create a dropdown menu with two possible variables
combobox = ttk.Combobox(frame, state="readonly", width=20)
combobox.pack(side="top", pady=5)
combobox["values"] = monitors[1:]
combobox.set(monitors[1])  # Set the first parameter by default

# Bind select event to the dropdown menu
combobox.bind("<<ComboboxSelected>>", on_select)

# Create a scale widget
scale_label = ttk.Label(root, text="Adjust Brightness ")
scale_label.grid(row=1, column=1, padx=10, pady=0, sticky="e")
scale = ttk.Scale(root, from_=1, to=100, orient="horizontal", command=change_brightness)
scale.set(50)  # Set initial value
scale.grid(row=1, column=2, padx=10, pady=10, sticky="w")


root.mainloop()
