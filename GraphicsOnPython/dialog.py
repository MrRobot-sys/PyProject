from tkinter import *
import Plotting

grap = Plotting.Graphics()


class DialogWindows(Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title('')