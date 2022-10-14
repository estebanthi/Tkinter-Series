import tkinter as tk
from tkinter import ttk

main_window = tk.Tk()
main_window.title("Widgets")
main_window.geometry("400x400")

main_window.grid_columnconfigure(0, weight=1)
main_window.grid_columnconfigure(1, weight=1)
main_window.grid_columnconfigure(2, weight=1)

scrollable_text_area = tk.Text(main_window, width=40, height=5)
scrollable_text_area.grid(row=0, column=0, columnspan=2, sticky=tk.EW, pady=5, padx=5)

scrollbar = ttk.Scrollbar(main_window, orient=tk.VERTICAL, command=scrollable_text_area.yview)
scrollbar.grid(row=0, column=2, sticky=tk.NS, pady=5, padx=5)

scrollable_text_area["yscrollcommand"] = scrollbar.set

separator = ttk.Separator(main_window, orient=tk.HORIZONTAL)
separator.grid(row=1, column=0, columnspan=3, sticky=tk.EW, pady=5, padx=5)

selected_value = tk.StringVar()

radio_button_1 = ttk.Radiobutton(main_window, text="Option 1", value="Option 1", variable=selected_value)
radio_button_1.grid(row=2, column=0, sticky=tk.W, pady=5, padx=5)

radio_button_2 = ttk.Radiobutton(main_window, text="Option 2", value="Option 2", variable=selected_value)
radio_button_2.grid(row=2, column=1, sticky=tk.W, pady=5, padx=5)

radio_button_3 = ttk.Radiobutton(main_window, text="Option 3", value="Option 3", variable=selected_value)
radio_button_3.grid(row=2, column=2, sticky=tk.W, pady=5, padx=5)

display_button = ttk.Button(main_window, text="Display", command=lambda: scrollable_text_area.insert(tk.END, f"{selected_value.get()} has been selected"))
display_button.grid(row=3, column=0, columnspan=3, sticky=tk.EW, pady=5, padx=5)

combobox_value = tk.StringVar()

combobox = ttk.Combobox(main_window, textvariable=combobox_value)
combobox["values"] = ("Option 1", "Option 2", "Option 3")
combobox["state"] = "readonly"
combobox.grid(row=4, column=0, columnspan=3, sticky=tk.EW, pady=5, padx=5)

items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
listbox = tk.Listbox(main_window, listvariable=tk.StringVar(value=items), height=3, selectmode=tk.MULTIPLE)
listbox.grid(row=5, column=0, columnspan=3, sticky=tk.EW, pady=5, padx=5)

label_frame = ttk.LabelFrame(main_window, text="Label Frame")
label_frame.grid(row=6, column=0, columnspan=3, sticky=tk.EW, pady=5, padx=5)

label_frame.grid_columnconfigure(0, weight=1)
label_frame.grid_columnconfigure(1, weight=1)
label_frame.grid_columnconfigure(2, weight=1)

button1 = ttk.Button(label_frame, text="Button 1")
button1.grid(row=0, column=0, sticky=tk.EW, pady=5, padx=5)

button2 = ttk.Button(label_frame, text="Button 2")
button2.grid(row=0, column=1, sticky=tk.EW, pady=5, padx=5)

button3 = ttk.Button(label_frame, text="Button 3")
button3.grid(row=0, column=2, sticky=tk.EW, pady=5, padx=5)

sizegrip = ttk.Sizegrip(main_window)
sizegrip.grid(row=7, column=2, sticky=tk.SE, pady=5, padx=5)

main_window.mainloop()