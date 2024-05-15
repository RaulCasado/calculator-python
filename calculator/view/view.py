# view/view.py

from tkinter import ttk

class ApplicationView:
    def __init__(self, master):
        self.master = master
        self.frm = ttk.Frame(master, padding=100)
        self.frm.grid()
        self.label = ttk.Label(self.frm, text="Counter: 0")
        self.label.grid(column=0, row=0)
        self.button = ttk.Button(self.frm, text="Increase")
        self.button.grid(column=1, row=0)

    def set_button_command(self, command):
        self.button.config(command=command)

    def update_counter_label(self, value):
        self.label.config(text=f"Counter: {value}")
