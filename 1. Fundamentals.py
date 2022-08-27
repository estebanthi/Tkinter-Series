import tkinter as tk
from tkinter import ttk

main_window = tk.Tk()
main_window.title("Hello World")

label = tk.Label(main_window, text="Hello World")
label.pack()

window_width = 500
window_height = 500

screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))

geometry = "{}x{}+{}+{}".format(window_width, window_height, center_x, center_y)
main_window.geometry(geometry)

main_window.resizable(False, False)

main_window.attributes("-alpha", 0.75)
main_window.iconbitmap("icon.ico")

new_label = ttk.Label(main_window, text="Hello World")
new_label.pack()
new_label["text"] = "Hi!"
new_label.config(text="Hello World")


def clicked():
    print("Button clicked!")


button = ttk.Button(main_window, text="Hello World!", command=clicked)
button.pack()


def callback(text):
    print(text)


button2 = ttk.Button(main_window, text="Hello World!", command=lambda: callback("Button 2 clicked!"))
button2.pack()

main_window.bind("<Button>", lambda event: callback("Button clicked!"))
main_window.unbind("<Button>")

main_window.mainloop()
