#En este segundo ejercicio, tendréis que crear una interfaz 
#sencilla la cual debe de contener una lista de elementos seleccionables,
#también debe de tener un label con el texto que queráis.

import tkinter
from tkinter import StringVar, ttk

window = tkinter.Tk()
window.columnconfigure(0,weight=5)
window.columnconfigure(1,weight=5)

listaElementos = ['1','2','3','4','5','6','7','8','9']
list_items = StringVar(value =listaElementos)
listbox = tkinter.Listbox(window,height =20,listvariable=list_items)
listbox.grid(column=0,row=0, sticky=tkinter.W)

etiquetaTexto = tkinter.Label(window,text = "Etiqueta",height=10, bg='red', fg='black')
etiquetaTexto.grid(column=1,row=0)

window.mainloop()