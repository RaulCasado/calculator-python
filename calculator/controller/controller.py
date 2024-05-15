# controller/controller.py

class ApplicationController:
    def __init__(self, master, calculator, view):
        self.master = master
        self.calculator = calculator
        self.view = view
        self.operation = ""
        self.view.initialize_buttons(self.control_buttons)

    def run(self):
        self.master.mainloop()

    def control_buttons(self,pressed_button):
        if pressed_button == "=":
            result = self.calculator.make_calculation(self.operation)
            self.view.show_result(result)
            return True
        self.operation += pressed_button
        self.view.update_result(pressed_button)