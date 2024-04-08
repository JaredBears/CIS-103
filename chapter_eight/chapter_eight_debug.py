# Here's a Python program with deliberate errors to debug. Find the errors and make the corrections.

import tkinter as tk



def fahrenheit_to_celsius():
    fahrenheit = float(entry_fahrenheit.get())
    celsius = (fahrenheit - 32) * 5/9
    label_result["text"] = f"{fahrenheit} Fahrenheit = {celsius:.2f} Celsius"

def celsius_to_fahrenheit():
    celsius = float(entry_celsius.get())
    fahrenheit = celsius * 9/5 + 32
    label_result["text"] = f"{celsius} Celsius = {fahrenheit:.2f} Fahrenheit"

root = tk.Tk()
root.title("Temperature Converter")

frame_fahrenheit = tk.Frame(root)
frame_fahrenheit.pack(pady=10)

label_fahrenheit = tk.Label(frame_fahrenheit, text="Fahrenheit:")
label_fahrenheit.pack(side="left")

entry_fahrenheit = tk.Entry(frame_fahrenheit)
entry_fahrenheit.pack(side="left")

frame_celsius = tk.Frame(root)
frame_celsius.pack(pady=10)

label_celsius = tk.Label(frame_celsius, text="Celsius:")
label_celsius.pack(side="left")

entry_celsius = tk.Entry(frame_celsius)
entry_celsius.pack(side="left")

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_fahrenheit_to_celsius = tk.Button(frame_buttons, text="Fahrenheit to Celsius", command=fahrenheit_to_celsius)
button_fahrenheit_to_celsius.pack(side="left")

button_celsius_to_fahrenheit = tk.Button(frame_buttons, text="Celsius to Fahrenheit", command=celsius_to_fahrenheit)
button_celsius_to_fahrenheit.pack(side="left")

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()
