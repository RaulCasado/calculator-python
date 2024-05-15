# controller/controller.py

class ApplicationController:
    def __init__(self, master, counter, view):
        self.master = master
        self.counter = counter
        self.view = view
        self.view.set_button_command(self.increase_counter)

    def increase_counter(self):
        self.counter.increase_counter()
        self.view.update_counter_label(self.counter.value)

    def run(self):
        self.master.mainloop()
