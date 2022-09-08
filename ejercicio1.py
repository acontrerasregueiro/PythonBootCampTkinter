#En este ejercicio tenéis que crear una lista de RadioButton
#que muestre la opción que se ha seleccionado y 
#que contenga un botón de reinicio para que deje todo como al principio.
#Al principio no tiene que haber una opción seleccionada.

import tkinter
from tkinter import StringVar, ttk
    
window = tkinter.Tk()
window.columnconfigure(0,weight=3) # Creamos una columna donde habrá 3 elementos

#Creamos los radio button
selected = StringVar()    
radio1 = ttk.Radiobutton(window,text="Opcion 1", value=1,variable=selected)
radio2 = ttk.Radiobutton(window,text="Opcion 2", value=2,variable=selected)
#Los posicionamos
radio1.grid(column=0,row=0,padx =5 , pady = 5)
radio2.grid(column=0,row=1,padx =5 , pady = 5)


#Creamos la funcion Reset
def funcionReset():
    selected.set(None)     # set(none) -> Deseleccionar el radio button

#Creamos el boton
boton_reset = ttk.Button(window,text= "Reset",command=funcionReset)
#Posicionamos el boton
boton_reset.grid(column=0,row=2,padx = 10, pady =10)

window.mainloop()