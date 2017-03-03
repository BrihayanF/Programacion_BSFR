import tkinter

from tkinter import messagebox

def accion_de_mi_boton():
    print('Mi primer boton ha sido precionado :v')
def accion_de_mi_segundo_boton():
    messagebox.showinfo('Primer dialogo emergente','Mi segundo boton ha sido precionado')
def accion_advertencia():
    messagebox.showwarning('Cuidado O.o','No debio precionar este boton, su ordenador se va a reiniciar')
# Crendo mi primera ventana
mi_ventana = tkinter.Tk()
mi_ventana.geometry('640x480')
mi_ventana.title('Mi primer programa :v')
# Crear mi primer boton :'v
mi_boton = tkinter.Button(text='Mi Boton', command = accion_de_mi_boton)
# Coloco mi boton en la ventana principal u.U
mi_boton.pack()
# Agregue mi segundo boton
mi_boton2 = tkinter.Button(text='Segundo boton', command = accion_de_mi_segundo_boton)
# Colocar mi segundo boton
mi_boton2.pack()
# Mostrar una advertencia
advertencia = tkinter.Button(text='No precionar >_<', command = accion_advertencia)
# Poner mi advertencia
advertencia.pack()
mi_ventana.mainloop()


