from tkinter import Tk
from controller.controller import ApplicationController
from model.model import Calculator
from view.view import ApplicationView

if __name__ == "__main__":
    root = Tk()
    calculator = Calculator()
    view = ApplicationView(root)
    app = ApplicationController(root, calculator, view)
    app.run()
