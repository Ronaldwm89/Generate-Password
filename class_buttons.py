from tkinter import Button
BG_COLOR = "grey"

class Botones(Button):
    def __init__(self, texto, col, rows, colspan, comando):
        super().__init__()
        self.config(text=texto, bg=BG_COLOR, fg="white", command=comando)
        self.grid(column=col, row=rows, columnspan=colspan)