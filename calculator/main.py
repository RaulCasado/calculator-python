# main.py

from tkinter import Tk
from controller.controller import ApplicationController
from model.model import Counter
from view.view import ApplicationView

if __name__ == "__main__":
    root = Tk()
    counter = Counter()
    view = ApplicationView(root)
    app = ApplicationController(root, counter, view)
    app.run()
