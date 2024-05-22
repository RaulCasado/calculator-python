from exceptions.parenthesis_exception import ParenthesisError

class ApplicationController:
    def __init__(self, master, calculator, view):
        self.master = master
        self.calculator = calculator
        self.view = view
        self.operation = ""
        self.view.initialize_buttons(self.control_buttons)
        self.view.bind_keyboard_event(self.on_key_pressed)

    def handle_calculation(self):
        """Handles the calculation and updates the view with the result."""
        result = "0"
        try:
            result = self.calculator.make_calculation(self.operation)
        except ParenthesisError as parenthesis:
            self.view.open_popup(parenthesis.message)
            return
        except Exception as e:
            self.view.open_popup("Ha ocurrido un error revise la cuenta")
            return
        self.view.show_result(result)
        self.operation = ""

    def handle_clear(self):
        """Clears the current operation and resets the calculator and view."""
        self.view.reset_result()
        self.operation = ""
        self.calculator.reset_previous_value()

    def handle_delete(self):
        """Deletes the last character in the current operation."""
        if self.operation:
            self.view.delete()
            self.operation = self.operation[:-1]

    def control_buttons(self, pressed_button):
        """Handles button press events."""
        actions = {
            "=": self.handle_calculation,
            "C": self.handle_clear,
            "<--": self.handle_delete
        }
    
        action = actions.get(pressed_button)
        if action:
            action()
        else:
            self.operation += pressed_button
            self.view.update_result(pressed_button)


    def on_key_pressed(self, event):
        """Handles keyboard events."""
        actions = {
            "=": self.handle_calculation,
            "\r": self.handle_calculation,  
            "c": self.handle_clear,
            "C": self.handle_clear,
            "\b": self.handle_delete       
        }
    
        action = actions.get(event.char)
        if action:
            action()
        else:
            self.operation += event.char
            self.view.update_result(event.char)


    def run(self):
        """Starts the main application loop."""
        self.master.mainloop()
