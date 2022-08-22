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
path = askdirectory(initialdir="~Desktop/Angeloni", title="Pasta destino")
print(path)

# Creates the folder
os.chdir(path)

# Asks the folder name
userStr = simpledialog.askstring(
    "Criar pasta",
    "Cole o título da task no Collab aqui. "
    "(Ex.: #0000: Cliente | Criação | Campanha | Peças 00/00)",
)

# Cleans the folder name
cleanStr1 = userStr.replace(":", "-")
cleanStr2 = cleanStr1.replace("/", "-")
cleanStr3 = cleanStr2.replace(".", "-")
NewFolder = cleanStr3

# Tests if the folder a ready exists
try:
    if not os.path.exists(NewFolder):
        os.makedirs(NewFolder)

    # Creates the subfolders
    path2 = path + "//" + NewFolder
    os.chdir(path2)
    NEWFOLDER_1 = "00_materiais"
    os.makedirs(NEWFOLDER_1)
    NEWFOLDER_2 = "01_layout"
    os.makedirs(NEWFOLDER_2)
    NEWFOLDER_3 = "02_view"
    os.makedirs(NEWFOLDER_3)

    # Success feedback
    tkinter.messagebox.showinfo("info", "Sucesso Total!")

# Error feedback
except OSError:
    tkinter.messagebox.showinfo(
        "info",
        "Erro: A pasta já existe! \
		                         Verifique o nome da task.",
    )
