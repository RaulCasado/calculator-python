from tkinter import ttk
import tkinter.messagebox

class ApplicationView:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("400x400")

        self.frm = ttk.Frame(master)
        self.frm.grid(padx=10, pady=10, sticky="nsew")

        self.result = ttk.Label(self.frm, text="0", anchor="e", font=("Helvetica", 20), width=10)
        self.result.grid(row=0, column=0, columnspan=4, pady=10)

        self.buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("(", 5, 1), (")", 5, 2), ("<--", 5, 3)
        ]

    def initialize_buttons(self, control_buttons_callback):
        for (text, row, column) in self.buttons:
            button = ttk.Button(self.frm, text=text, command=lambda t=text: control_buttons_callback(t))
            button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

    def update_result(self, value_to_update):
        full_text = value_to_update if self.result.cget("text") == "0" else self.result.cget("text") + value_to_update
        self.result.config(text=full_text)

    def show_result(self, value):
        self.result.config(text=value)

    def bind_keyboard_event(self, handler):
        for key in range(10):
            self.master.bind(str(key), handler)

        operators = ["+", "-", "*", "/", "=", "<Return>", "c", "C", "(", ")"]
        for op in operators:
            self.master.bind(op, handler)

    def reset_result(self):
        self.result.config(text="0")

    def open_popup(self, message):
        tkinter.messagebox.showinfo("Mensaje", message)
