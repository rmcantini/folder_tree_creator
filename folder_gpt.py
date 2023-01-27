""" import os and tk """
import os
from tkinter import simpledialog
from tkinter.filedialog import askdirectory
import tkinter.messagebox
import tkinter as tk

# hide root window
root = tk.Tk()
root.withdraw()

# Intro guide messagebox
tkinter.messagebox.showinfo(
    "info", "Selecione onde será salva a task, \n(Super ou Eletro)."
)

# Shows dialog box and return the path
path = askdirectory(
    initialdir="/Volumes/Cadastra/CANTINI/Clientes/Angeloni", title="Pasta destino"
)

# Creates the folder
os.makedirs(
    os.path.join(path, userStr.replace(":", " |").replace("/", "-")), exist_ok=True
)

# Creates the subfolders
path2 = path + "//" + userStr.replace(":", " |").replace("/", "-")
os
