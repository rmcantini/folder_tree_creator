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
    'info', 'Selecione onde será salva a task, \n(Super ou Eletro).')

# Shows dialog box and return the path
path: str = askdirectory(
    initialdir='/Volumes/Cadastra/CANTINI/Clientes/Angeloni',
    title='Pasta destino'
)
print(path)

# Creates the folder
os.chdir(path)

# Asks the folder name
userStr: str = simpledialog.askstring(
    'Criar pasta', 'Cole o título da task no Collab aqui. \n'
    + '(Ex.: #0000: Cliente | Criação | Campanha | Peças 00/00)'
)

# Cleans the folder name
cleanStr1: str = userStr.replace(':', ' |')
cleanStr2: str = cleanStr1.replace('/', '-')
NewFolder: str = cleanStr2

# Tests if the folder a ready exists
try:
    if not os.path.exists(NewFolder):
        os.makedirs(NewFolder)

    # Creates the subfolders
    path2: str = path + '/' + NewFolder
    os.chdir(path2)
    NEWFOLDER_1: str = '00_materiais'
    os.makedirs(NEWFOLDER_1)
    NEWFOLDER_2: str = '01_layout'
    os.makedirs(NEWFOLDER_2)
    NEWFOLDER_3: str = '02_view'
    os.makedirs(NEWFOLDER_3)

    # Success feedback
    tkinter.messagebox.showinfo('info', 'Sucesso Total!')

# Error feedback
except OSError:
    tkinter.messagebox.showinfo('info', 'Erro: A pasta já existe! \n'
                               + 'Verifique o nome da task.')
