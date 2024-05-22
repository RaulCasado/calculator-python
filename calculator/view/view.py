from tkinter import ttk, Text, Tk
import tkinter.messagebox

class ApplicationView:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("1400x400")

        self.frm = ttk.Frame(master)
        self.frm.grid(padx=10, pady=10, sticky="nsew")

        self.result = Text(self.frm, height=2, font=("Helvetica", 20), wrap="none")
        self.result.grid(row=0, column=0, columnspan=4, pady=10)
        self.result.insert("1.0", "0")
        self.result.config(state="disabled")

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
        self.result.config(state="normal")
        current_text = self.result.get("1.0", "end-1c")
        new_text = value_to_update if current_text == "0" else current_text + value_to_update
        self.result.delete("1.0", "end")
        self.result.insert("1.0", new_text)
        self.result.config(state="disabled")

    def show_result(self, value):
        self.result.config(state="normal")
        self.result.delete("1.0", "end")
        self.result.insert("1.0", value)
        self.result.config(state="disabled")

    def delete(self):
        self.result.config(state="normal")
        text = self.result.get("1.0", "end-1c")
        new_text = text[:-1] if len(text) > 1 else "0"
        self.show_result(new_text)
        self.result.config(state="disabled")

    def bind_keyboard_event(self, handler):
        for key in "0123456789":
            self.master.bind(key, handler)
        operators = ["+", "-", "*", "/", "=", "<Return>", "c", "C", "(", ")", "<Key-BackSpace>"]
        for op in operators:
            self.master.bind(op, handler)

    def reset_result(self):
        self.show_result("0")

    def open_popup(self, message):
        tkinter.messagebox.showinfo("Mensaje", message)