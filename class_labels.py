from tkinter import Label
RED = "#B5EAEA"
BG_COLOR = "#068DA9"
FONT = ("times new roman", 12, "normal")
class Labels(Label):
    def __init__(self,texto, cols ,rows):
        super().__init__()
        self.config(text=texto, bg= BG_COLOR, font=FONT, fg=RED)
        self.grid(column=cols, row=rows)