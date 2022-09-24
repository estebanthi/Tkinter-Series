import tkinter as tk
from tkinter import ttk


main_window = tk.Tk()
main_window.title("Widgets")
main_window.geometry("400x400")

frame = ttk.Frame(main_window, padding=10)
frame.pack()

text_area = tk.Text(frame, width=40, height=10)
text_area.insert(tk.END, "Hello World!")
text_area.pack()

print(text_area.get("1.0", tk.END))
text_area.delete("1.0", tk.END)
text_area["state"] = tk.NORMAL
text_area["state"] = tk.DISABLED

is_checked = tk.BooleanVar()
checkbox = ttk.Checkbutton(frame, text="Check me!", variable=is_checked, onvalue=True, offvalue=False, command=lambda: print(is_checked.get()))
checkbox.pack()

current_value = tk.IntVar()
slider = ttk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: print(current_value.get()), variable=current_value)
slider.pack()

spinbox_value = tk.IntVar()
spinbox = ttk.Spinbox(frame, from_=0, to=100, command=lambda: print(spinbox_value.get()), textvariable=spinbox_value)
spinbox.pack()

main_window.mainloop()
