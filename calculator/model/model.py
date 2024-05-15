# model/counter.py

class Calculator:
    def __init__(self):
        self.value = 0

    def make_calculation(self,operation):
        return str(eval(operation[1:]))
