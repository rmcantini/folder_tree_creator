#import os and tk
import os
from tkinter import Tk, simpledialog
from tkinter.filedialog import askdirectory
import tkinter.messagebox
#hide root window
import tkinter as tk 
root = tk.Tk() 
root.withdraw()
#intro guide messagebox
tkinter.messagebox.showinfo('info', 'Selecione onde será salva a task')
#Shows dialog box and return the path
path=askdirectory(title='Selecione a pasta') 
print(path)
#Creates the folder
os.chdir(path)
#Asks the folder name
userStr=simpledialog.askstring('Criar pasta', 'Cole o título da task no Collab aqui. (Ex.: #0000: Cliente | Criação | Campanha | Peças 00/00)')
print=(userStr)
#Cleans the folder name
cleanStr1=userStr.replace(':', ' |')
print=(cleanStr1)
cleanStr2=cleanStr1.replace('/', '-')
print=(cleanStr2)
NewFolder=cleanStr2
#tests if the folder already exists
try:
	if not os.path.exists(NewFolder):
		os.makedirs(NewFolder)
	#Folders inside the main one
	path2=path+'//'+NewFolder
	os.chdir(path2)
	NewFolder_1='00_materiais'
	os.makedirs(NewFolder_1)
	NewFolder_2='01_editaveis'
	os.makedirs(NewFolder_2)
	NewFolder_3='02_img'
	os.makedirs(NewFolder_3)
	#Success feedback	
	tkinter.messagebox.showinfo('info', 'Sucesso Total!')
#Error feedback

except OSError:
	tkinter.messagebox.showinfo('info', 'Erro: A pasta já existe! Verifique o nome da task.')
root.destroy()