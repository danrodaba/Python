import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *

app = tk.Tk() #Ventana raiz de la app
app.title("Ola que ase?") #El nombre de la ventana
app.resizable(True,False) #app.resizable(0,0) desactivaría la redimensión de la ventana
app.iconbitmap('tkinter/pokemon.ico') #fichero con el icono de la ventana. Deber ser .ico
app.geometry('800x500') #tamaño de la ventana inicial

imagen = ImageTk.PhotoImage(file='tkinter/pokemon.jpg') #aquí se coje la imagen
etiqueta = Label(app,image=imagen).pack() #pack() es para que sitúe la imagen al inicio de la ventana
app.state('zoomed')
#etiqueta.place(x = 100, y = 50)


app.mainloop()