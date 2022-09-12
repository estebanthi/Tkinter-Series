import tkinter as tk
from tkinter import ttk


class LoginFormApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Form")
        self.geometry("220x100")
        self.create_widgets()

    def create_widgets(self):
        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=0, sticky=tk.W, pady=5, padx=5)

        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=0, column=1, sticky=tk.W, pady=5, padx=5)

        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)

        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, sticky=tk.W, pady=5, padx=5)

        self.login_button = ttk.Button(self, text="Login")
        self.login_button.grid(row=2, column=0, columnspan=2, sticky=tk.EW, pady=5, padx=5)


if __name__ == "__main__":
    app = LoginFormApp()
    app.mainloop()
