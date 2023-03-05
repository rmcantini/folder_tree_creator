""" import os and tk """
import os
from tkinter import simpledialog, filedialog, messagebox
import tkinter as tk

# hide root window
root = tk.Tk()
root.withdraw()

# Intro guide messagebox
messagebox.showinfo("info", "Selecione onde será salva a task, \n(Super ou Eletro).")

# Shows dialog box and return the path
path = filedialog.askdirectory(
    initialdir="/Volumes/Cadastra/CANTINI/Clientes/Angeloni", title="Pasta destino"
)
print(path)

# Creates the folder
os.chdir(path)

# Asks the folder name
user_str = simpledialog.askstring(
    "Criar pasta",
    "Cole o título da task no Collab aqui. (Ex.: #0000: Cliente | Criação | Campanha | Peças 00/00)",
)

# Cleans the folder name
clean_str = user_str.replace(":", " |").replace("/", "-")
new_folder = clean_str

# Tests if the folder already exists
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

    # Creates the subfolders
    path2 = os.path.join(path, new_folder)
    os.chdir(path2)
    os.makedirs("00_materiais")
    os.makedirs("01_layout")
    os.makedirs("02_view")

    # Success feedback
    messagebox.showinfo("info", "Sucesso Total!")
else:
    # Error feedback
    messagebox.showinfo("info", "Erro: A pasta já existe! Verifique o nome da task.")

"""
Changes made:

    Removed unnecessary imports and combined multiple imports from the same module into a single import line.
    Renamed variables to follow Python's style guide.
    Simplified folder name cleaning using method chaining.
    Removed unnecessary try-except block and replaced it with an if-else statement.
    Replaced string concatenation with os.path.join() for creating folder paths.
"""
