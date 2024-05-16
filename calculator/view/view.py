from tkinter import ttk
import tkinter.messagebox

class ApplicationView:
    def __init__(self, master):
        self.master = master
        self.frm = ttk.Frame(master, padding=100)
        self.frm.grid()
        self.result = ttk.Label(self.frm, text="0")
        self.result.grid(column=0, row=0)
        self.buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("(", 5, 3), (")", 6 ,3),
        ]

    def initialize_buttons(self,control_buttons_callback):
        for (text, row, column) in self.buttons:
            button = ttk.Button(self.frm, text=text, command=lambda t=text: control_buttons_callback(t))
            button.grid(row=row, column=column, padx=5, pady=5)

    def update_result(self,value_to_update):
        full_text = value_to_update if self.result.cget("text") == "0" else self.result.cget("text") + value_to_update
        self.result.config(text = full_text)

    def show_result(self,value):
        self.result.config(text=value)

    def bind_keyboard_event(self, handler):
        for key in range(10):
            self.master.bind(str(key), handler)

        operators = ["+", "-", "*", "/", "=",'<Return>',"c","C","(",")"]
        for op in operators:
            self.master.bind(op, handler)

    def reset_result(self):
        self.result.config(text="0")

    def open_popup(self, message):
        tkinter.messagebox.showinfo("Mensaje", message)
