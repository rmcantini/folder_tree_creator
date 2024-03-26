"""Creates a new folder with the title provided
by the user, and then creates three subfolders inside it"""
import os
import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox

# Hide root window
root = tk.Tk()
root.withdraw()

# Intro guide messagebox
messagebox.showinfo("Info", "Selecione onde será salva a task, (Super ou Eletro).")

# Shows dialog box and return the path
path = filedialog.askdirectory(
    initialdir="/Volumes/Cadastra/CANTINI/Clientes/Angeloni",
    title="Pasta destino")
print(path)

# Creates the folder
os.chdir(path)

# Asks the folder name
userStr = simpledialog.askstring(
    "Criar pasta", "Cole o título da task no Collab aqui.\n \
        (Ex.: #0000: Cliente | Criação | Campanha | Peças 00/00)")

# Cleans the folder name
cleanStr1 = userStr.replace(":", " |")
cleanStr2 = cleanStr1.replace("/", "-")
NewFolder = cleanStr2

# Tests if the folder a ready exists
try:
    if not os.path.exists(NewFolder):
        os.makedirs(NewFolder)

    # Creates the subfolders
    path2 = f"{path}\\{NewFolder}"
    NEWFOLDER_1 = "00_materiais"
    os.makedirs(NEWFOLDER_1)
    NEWFOLDER_2 = "01_layout"
    os.makedirs(NEWFOLDER_2)
    NEWFOLDER_3 = "02_view"
    os.makedirs(NEWFOLDER_3)

    # Success feedback
    messagebox.showinfo("Info", "Sucesso Total!")

# Error feedback
except OSError as err:
    messagebox.showinfo("Error", f"Error: {err}.\n\
        Verify the name of the task.")
