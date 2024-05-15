# model/counter.py

class Calculator:
    def __init__(self):
        self.value = 0

    def make_calculation(self,operation):
        if operation == "":
            return "0"
        return str(eval(operation))
