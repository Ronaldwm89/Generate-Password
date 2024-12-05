from tkinter import Entry

class Entradas(Entry):
    def __init__(self, widths, cols, rows, colspan):
        super().__init__()
        self.config(width=widths)
        self.grid(column=cols, row=rows, columnspan=colspan)
