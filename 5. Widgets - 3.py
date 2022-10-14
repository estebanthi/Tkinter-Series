import tkinter as tk
from tkinter import ttk
import time
import random

main_window = tk.Tk()
main_window.title("Widgets")
main_window.geometry("400x400")

main_window.grid_columnconfigure(0, weight=1)
main_window.grid_columnconfigure(1, weight=1)
main_window.grid_columnconfigure(2, weight=1)

paned_window = ttk.Panedwindow(main_window, orient=tk.HORIZONTAL)
paned_window.grid(column=0, row=0, sticky="we", columnspan=3, rowspan=3)

button_left = ttk.Button(paned_window, text="Left")
paned_window.add(button_left, weight=1)

button_right = ttk.Button(paned_window, text="Right")
paned_window.add(button_right, weight=1)

progress_bar = ttk.Progressbar(main_window, orient=tk.HORIZONTAL, length=200, mode="determinate", maximum=100)
progress_bar.grid(column=0, row=3, sticky="we", columnspan=3)


def start_progress():
    progress_bar_value = progress_bar["value"]
    for i in range(10):
        progress_bar_value += 10
        progress_bar["value"] = progress_bar_value
        main_window.update_idletasks()
        time.sleep(0.05)


start_button = ttk.Button(main_window, text="Start", command=start_progress)
start_button.grid(column=0, row=4, sticky="we")

stop_button = ttk.Button(main_window, text="Stop", command=progress_bar.stop)
stop_button.grid(column=2, row=4, sticky="we")

notebook = ttk.Notebook(main_window)
notebook.grid(column=0, row=5, sticky="we", columnspan=3)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text="Frame 1")
notebook.add(frame2, text="Frame 2")

frame1.grid_columnconfigure(0, weight=1)
frame1.grid_columnconfigure(1, weight=1)
frame1.grid_columnconfigure(2, weight=1)

frame2.grid_columnconfigure(0, weight=1)
frame2.grid_columnconfigure(1, weight=1)
frame2.grid_columnconfigure(2, weight=1)

label1 = ttk.Label(frame1, text="Label 1")
label1.grid(column=0, row=0, sticky="we", columnspan=3)

label2 = ttk.Label(frame2, text="Label 2")
label2.grid(column=0, row=0, sticky="we", columnspan=3)

tree_view = ttk.Treeview(frame1, columns=("Id", "Age", "Genre"), show="headings")

tree_view.column("Id", width=100, anchor="center")
tree_view.column("Age", width=100, anchor="center")
tree_view.column("Genre", width=100, anchor="center")

tree_view.heading("Id", text="Id")
tree_view.heading("Age", text="Age")
tree_view.heading("Genre", text="Genre")

persons = [(_id, age, genre) for _id, age, genre in zip([random.randint(1000, 100000) for _ in range(10)], [random.randint(1, 100) for _ in range(10)], [random.choice(['M', 'F']) for i in range(10)])]
for person in persons:
    tree_view.insert("", tk.END, values=person)

tree_view.bind("<<TreeviewSelect>>", lambda event: tree_view.delete(tree_view.selection()))

tree_view.grid(column=0, row=6, sticky="we", columnspan=3)

canvas = tk.Canvas(frame2, width=200, height=200)
canvas.grid(column=0, row=1, sticky="we", columnspan=3)

canvas.create_line(0, 0, 200, 200, fill="red", width=5)
canvas.create_oval(0, 0, 200, 200, fill="blue", outline="red", width=5)
canvas.create_rectangle(0, 0, 200, 200, fill="green", outline="red", width=5)
canvas.create_arc(0, 0, 200, 200, fill="yellow", outline="red", width=5, start=0, extent=180)
canvas.create_polygon(0, 0, 200, 200, 0, 200, fill="purple", outline="red", width=5)
canvas.create_text(100, 100, text="Hello World", fill="red", font=("Arial", 20))

cursor = "arrow"
def change_cursor(event):
    global cursor
    if cursor == "arrow":
        cursor = "pencil"
    else:
        cursor = "arrow"
    canvas.config(cursor=cursor)

canvas.bind("<Button-1>", change_cursor)

main_window.mainloop()