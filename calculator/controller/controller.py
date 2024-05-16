class ApplicationController:
    def __init__(self, master, calculator, view):
        self.master = master
        self.calculator = calculator
        self.view = view
        self.operation = ""
        self.view.initialize_buttons(self.control_buttons)
        self.view.bind_keyboard_event(self.on_key_pressed)

    def run(self):
        self.master.mainloop()

    def control_buttons(self,pressed_button):
        if pressed_button == "=":
            result = self.calculator.make_calculation(self.operation)
            self.view.show_result(result)
            return True
        if pressed_button == "C":
            self.view.reset_result()
            self.operation = ""
            return True
        self.operation += pressed_button
        self.view.update_result(pressed_button)
    
    def on_key_pressed(self, event):
        if event.char == "=" or event.char == "\r":
            result = self.calculator.make_calculation(self.operation)
            self.view.show_result(result)
            return True
        if event.char == "c" or event.char == "C":
            self.view.reset_result()
            self.operation = ""
            return True
        self.operation += event.char
        self.view.update_result(event.char)