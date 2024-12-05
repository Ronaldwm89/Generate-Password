# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
from class_labels import Labels
from class_entrys import Entradas
from class_buttons import Botones
from modulo_abc import *
import random
import pyperclip



def password_aleatoria():
    
    password_generate = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_generate += [random.choice(numbers) for _ in range(random.randint(2,4))]
    password_generate += [random.choice(symbols) for _ in range(random.randint(2,4))]

    random.shuffle(password_generate)
    password_g = "".join(password_generate)
    return password_g

def save():
    website_text = inp_website.get()
    email_text = inp_email.get()
    passw_text = inp_passw.get()

    if len(website_text) < 1 or len(passw_text) < 1:
        messagebox.showinfo(title="Input Empty", message="Debes completar todos los campos")
        
    else:
        validacion = messagebox.askokcancel(title=website_text, message=f"Desea guardar la siguiente informacion:\n Email: {email_text}\n Contraseña: {passw_text}\n OK?")

        if validacion:
            with open(r"passwords.txt", "a") as data:
            
             data.write(f"{website_text} | {email_text} | {passw_text}\n")
             inp_passw.delete(0, END)
             inp_website.delete(0, END)
             inp_website.focus()

def generate():
    contraseña = password_aleatoria()
    inp_passw.insert(0, contraseña)
    pyperclip.copy(contraseña)
    

BLUE = "#30475E"
RED = "#F05454"
BG_COLOR = "#068DA9"

root = Tk()
root.title("Password Generator")
root.config(padx=100, pady=100, bg= BG_COLOR)
image_bg = PhotoImage(file= r"logo.png")

canvas_bg = Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
canvas_bg.create_image(100,100, image=image_bg)
canvas_bg.grid(column=1, row=0)


website = Labels("Website:", 0,1)
email_user = Labels("Email/Username:", 0,2)
password = Labels("Password:", 0,3)

button_generate = Botones("Generate", 2,3,1, generate)
button_add = Botones("Add", 1,4,2, save)

button_add.config(width=34)

inp_website = Entradas(40,1,1,2)
inp_website.focus()

inp_email = Entradas(40,1,2,2)
inp_email.insert(0, "ronaldwmm1989@gmail.com")

inp_passw = Entradas(30,1,3,1)


root.mainloop()