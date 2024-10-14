from exceptions.parenthesis_exception import ParenthesisError

class ApplicationController:
    def __init__(self, master, calculator, view):
        self.master = master
        self.calculator = calculator
        self.view = view
        self.operation = ""
        self.view.initialize_buttons(self.control_buttons)
        self.view.bind_keyboard_event(self.on_key_pressed)

    def control_buttons(self, pressed_button):
        actions = {
            "=": self.handle_calculation,
            "C": self.handle_clear,
            "<--": self.handle_delete
        }
        if pressed_button in actions:
            actions[pressed_button]()
        else:
            self.operation += pressed_button
            self.view.update_result(pressed_button)

    def handle_calculation(self):
        try:
            result = self.calculator.make_calculation(self.operation)
            self.view.show_result(result)
        except ParenthesisError:
            self.view.open_popup("Los paréntesis no son válidos")
        except Exception:
            self.view.open_popup("Revise la cuenta por favor")
        finally:
            self.operation = ""

    def handle_clear(self):
        self.view.reset_result()
        self.operation = ""
        self.calculator.reset_previous_value()

    def handle_delete(self):
        if self.operation:
            self.view.delete()
            self.operation = self.operation[:-1]

    def on_key_pressed(self, event):
        key = event.char

        key_actions = {
            "\r": self.handle_calculation,
            "c": self.handle_clear,
            "C": self.handle_clear,
            "\b": self.handle_delete
        }

        if key in key_actions:
            key_actions[key]()
        elif key in "0123456789+-*/()":
            self.control_buttons(key)

    def run(self):
        self.master.mainloop()
