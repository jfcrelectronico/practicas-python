# import tkinter as tk
# from tkinter import ttk # aqui estan alojadas las definiciones de los componentes o widgets
#
# from controlador.eventos import btn_inicio
#
# logo_itohix = "C:/proyectos_python/tkinter/imagenes/IOTHIX-LIGHT-firma.ico"# establecer la ruta donde esta el icono de la ventana
# #creacion de objeto tkinter
# interfaces_tk=tk.Tk()#se crea el objero interfaces_tk mediante el constructor Tk()
# #Modificar tamaño de la ventana por default cuando se lanza la aplicacion por pixeles (ancho x alto)
# interfaces_tk.geometry('1280x720')
# #cambiar nombre de la ventana
# interfaces_tk.title("IoThix")
#
# #configurando icono de la aplicacion
# #se requiere una imagen con extension .ico, para este caso se agrego el logo de IoThix a la carpeta raiz
# interfaces_tk.iconbitmap(logo_itohix)
#
# # crear un componente o widget, cuando se crean componentes simpre se debe especificar cual es el objeto padre donde
# #se ubicara, para este caso estara en el objeto interfaces_tk que es la ventana que se esta creando
# #los componentes hacen parte de otro paquete de python que se denomina ttk
#
#
# def btn_inicio_local():
#     print("Evento del boton")
#     boton1.config(text="Boton presionado")# cambiar la propiedad text del boton1
#     boton2=ttk.Button(interfaces_tk,text="Boton creado")
#     boton2.pack()#habilita la visualizacion del boton y que se ubique de fortma automatica
#
#
#
#
#
# #se indica como se menciono anteriormente el objeto padre donde se desplegara el boton y se indico el texto que tendra el mismo
# boton1=ttk.Button(interfaces_tk,text="Boton de inicio",command=btn_inicio_local)# command permite definir como se manejan los eventos en el boton
# #para desplegar los componetes o widgets se utiliza PLM(pack layout manager) y que se ubiquen de forma automatica
# boton1.pack()
# #lanzar la interface, la misma debe ser lanzada despues de todos los ajustes que se realizan a la GUI
# # si este metodo no es llamado la interface NO sera desplegada
# interfaces_tk.mainloop()


import sys
import tkinter as tk
from tkinter import ttk,messagebox,Menu

icono="C:/proyectos_python/tkinter/imagenes/IOTHIX-LIGHT-firma.ico"

ventana_principal=tk.Tk()
ventana_principal.title("Iothix_grid")
ventana_principal.iconbitmap(icono)
ventana_principal.geometry("600x400")



# AJUSTAR el tamaño de los elementos ubicados en una celda especifica para ocupar un espacio proprocinal en toda la pantalla respecto
#al tamaño total de la GUI

ventana_principal.columnconfigure(0,weight=1)# se indica el ancho de los componentes de la columna 0 respecto al tamaño total disponible GUI
ventana_principal.rowconfigure(0,weight=1)## se indica el ancho de los componentes de la fila 0 respecto al tamaño total disponible GUI
ventana_principal.columnconfigure(1,weight=3)
#ventana_principal.rowconfigure(1,weight=2)

ventana_principal.columnconfigure(2,weight=3)


def fcn_btn1():
    boton1.config(text="Btn 1 fue presionado")
boton1=ttk.Button(ventana_principal,text="Btn 1",command=fcn_btn1)

#manejo con grid para posicionar componetes o widgets

boton1.grid(row=0,column=0,sticky="NSWE")# se especifica la posicion deseada del grid


def fcn_btn2():
    boton2.config(text="Btn 2 fue presionado")
    messagebox.showerror("etiqueta ventana emergente", "Mensaje error")
boton2=ttk.Button(ventana_principal,text="Btn 2",command=fcn_btn2)

boton2.grid(row=1,column=0,sticky="NSWE")# con sticky se forza a que el boton ocupe todo el espacio dsiponeble en la celda de arriba a abajo

def fcn_btn3():
    boton3.config(text="Btn 3 fue \n presionado")
    messagebox.showwarning("etiqueta ventana emergente", "Mensaje advertancia")

boton3=ttk.Button(ventana_principal,text="Btn 3",command=fcn_btn3)

boton3.grid(row=0,column=1,sticky="NSWE",padx=50,pady=30,ipadx=50)# con sticky se obliga al boton a ajustarse dentro dentro se su celda a la izquierda asi el espacio de la misma se aumente


def fcn_btn4():
    boton4.config(text="Btn 4fue \n presionado")

boton4=ttk.Button(ventana_principal,text="Btn 4",command=fcn_btn4)
#boton4.grid(row=1,column=1,sticky="NSWE")# con sticky se obliga al boton a ajustarse dentro dentro se su celda a la izquierda asi el espacio de la misma
                                                                  # genera separacion del componente cuando ya el mismo esta ubicado de los lementos al rededor
                                                                  # permite que el espacio ubicado por el componente se mas amplio respecto a lo indicado
                                                                  # por las propiedades padx y pady.
def fcn_btn5():
    boton5.config(text="Btn 5fue \n presionado")
    messagebox.showinfo("etiqueta ventana emergente","Mensaje informativo")
boton5=tk.Button(ventana_principal,text="Btn 5",command=fcn_btn5, fg='blue')# fg permite cambiar el colo de la fuente
boton5.grid(row=0,column=2,sticky="NSWE")# con sticky se obliga al boton a ajustarse dentro dentro se su celda a la izquierda asi el espacio de la misma

def fcn_btn6():
    boton6.config(text=var_texto1.get())
    print(texto1.get())
    boton3.config(text=texto1.get())# asignar el texto contenido en el widget texto y asignarlo al texto del boton3
    #texto1.delete(0,tk.END)#Eliminar el texto ingresado en el componente texto1 desde el inicio hasta el caracter final.
    texto1.select_range(0,tk.END)#seleccionar texto en widget entry
    texto1.focus()#resaltar el texto seleccionado con el metodo select_range
    var_texto1.set('valor nuevo')
    print(var_texto1.get())
    etiqueta_texto1.config(text="boton6 accionado")
boton6=tk.Button(ventana_principal,text="Btn 6",command=fcn_btn6, relief=tk.GROOVE,background='darkblue')#relief aplica un relieve al boton,background cambia el color de fondo del boton
boton6.grid(row=1,column=2,sticky="NSWE")# con sticky se obliga al boton a ajustarse dentro dentro se su celda a la izquierda asi el espacio de la misma




var_texto1=tk.StringVar(value='Valor por defecto')#variable a asociar al componente del tipo Entry
texto1=ttk.Entry(ventana_principal,width=16,state=tk.NORMAL,textvariable=var_texto1)#crear un elemento para ingresar texto, width determina la cantidad de caracteres que se mostraran en simultanea en el componente
                                           #la propiedad justify permite definir el tipo de alineacion que se le dara al texto por defecto es izquierda.
                                           #state habilita o desabilita la interaccion con la caja de texto
                                           #textvariable permite asociar el valor de una variable al componente entry.

#texto1.insert(0,"ABCDE")# texto por defecto en el componente ENTRY
#texto1.insert(tk.END,'=prim')#el metodo END permite insertar al final del componente texto1 una cadena deseada
#texto1.config(state='readonly')#solo permite la lectura del texto dentro del componente ENTRY el mismo no puede ser editado

texto1.grid(row=1,column=1)

etiqueta_texto1=tk.Label(ventana_principal,text="Ingrese texto")
etiqueta_texto1.grid(row=2,column=1)

def salir():
    ventana_principal.quit()#cerrar objeto
    ventana_principal.destroy()#destruir objeto
    sys.exit()#cerrar aplicacion

def menu_gui():
    #crear objeto Menu y lo situa en la vantana principal
    menu_principal=Menu(ventana_principal)

    # submenu_archivo es un componente hijo de menu_principal que a su vez es un componete hijo de ventana_principal
    # tearoff se le debe asignar false para evitar que el menu se separe de la GUI, de no ser asi al seleccionar una opcion se desplegara otra ventana
    submenu_archivo=Menu(menu_principal,tearoff=False)
    #agregar una opciones comando al submenu_archivo
    submenu_archivo.add_command(label='Nuevo')
    submenu_archivo.add_separator()# agregar una linea de separacion entre las opciones del submenu
    submenu_archivo.add_command(label='Salir',command=salir)#al presionar la opcion salir se llama a la funcion salir que cierra el objeto ventana principal, lo destruye y cierra completamente la aplicacion lanzada
    #agregar el submenu_archivo al menu_principal para que se despliegue en modo cascada y etiquetar el menu_principal con la palabra Archivo
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')

    #submenu_ayuda
    submenu_ayuda = Menu(menu_principal, tearoff=False)
    # agregar una opciones comando al submenu_archivo
    submenu_ayuda.add_command(label='Acerca de')
    menu_principal.add_cascade(menu=submenu_ayuda, label='Ayuda')

    #mostrar el menu en la ventana principal, a diferencia de los widgets los menus no se activan mediante el uso del metodo grid
    ventana_principal.config(menu=menu_principal)

menu_gui()




ventana_principal.mainloop()