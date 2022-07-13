import tkinter as tk
from tkinter.filedialog import askopenfile,asksaveasfilename # permite la interacion con archivos almacenados en la maquina



class editorTexto(tk.Tk):# Heredar de la clase padre el constructor

    def __init__(self):
        super().__init__()#siempre se inicializan primero las clases padre
        #self.geometry('600x400+400+200')  # 600x 400 indica el tamaño de la ventana, mientras +400+200 la posicion en pantalla en la cual se desplegara la ventana inicialmente
        self.rowconfigure(0,minsize=600,weight=1)# como la aplicacion solo tendra una fila(0) se ajusta el tamaño minimo de esta fila en 600px.
        self.columnconfigure(1,minsize=600,weight=1)# la columna 1 corresponde a la ubicacion del editor de texto.
        self.archivo = None  # almacenara la ruta del archivo seleccionado al presionar el boton abrir
        self.archivo_abierto=False #permitira conocer su al presionar el boton guardar se tiene un archivo existente ya abierto y simplemente se sobreescribe
                                   #o si por el contratio no existe un archivo y se debe abrir la ventana emergente
        self.title(self.archivo)
        self.iconbitmap('icono.ico')
        self.editor_texto=tk.Text(self,wrap=tk.WORD)#el parametro wrap permite que la separacion de palabras al llegar la limite ancho del editor de texto
                                                    #se realice en palabras completas y no por letras
        self._crear_componentes()
        self._crear_menu()

    def _crear_componentes(self):
        botonesFrame=tk.Frame(self,relief=tk.RAISED,bd=2)#el parametro relief permite resaltar un componente para que visualmente se diferencie de la ubicacion de los demas
        btnAbrir=tk.Button(botonesFrame,text='Abrir',command=self._abrirArchivo)
        btnGuardar = tk.Button(botonesFrame, text='Guardar',command=self._guardarArchivo)
        btnGuardarComo = tk.Button(botonesFrame, text='Guardar Como ...',command=self._guardarArchivoComo)
        btnAbrir.grid(row=0,column=0,sticky='we',padx=5,pady=5)# sticky forza al boton a usar todo el espacio que tenga disponible
        btnGuardar.grid(row=1, column=0, sticky='we', padx=5,pady=5)  # sticky forza al boton a usar ancho todo el espacio que tenga disponible
        btnGuardarComo.grid(row=2, column=0, sticky='we', padx=5,pady=5)  # sticky forza al boton a usar todo el espacio que tenga disponible
        botonesFrame.grid(row=0,column=0,sticky='ns')# sticky forza al boton a usar todo el espacio que tenga disponible
        self.editor_texto.grid(row=0,column=1,sticky='nswe')#agregar el widget tipo text a la interface

    def _crear_menu(self):
        menu_app=tk.Menu(self)
        self.config(menu=menu_app)#para los menus esta es la forma de hacer que se muestren en pantalla al igual que en algunos elementos se usa grid o pack
        #agregando las opciones del menu
        opcionesMenu=tk.Menu(menu_app,tearoff=False)#tearoff liga al menu a la ventana donde se despliega
        opcionesMenu.add_command(label='Abrir',command=self._abrirArchivo)
        opcionesMenu.add_command(label='Guardar',command=self._guardarArchivo)
        opcionesMenu.add_command(label='Guardar Como...',command=self._guardarArchivoComo)
        opcionesMenu.add_separator()
        opcionesMenu.add_command(label='Salir',command=self.quit)#opcion salir agregada al menu
        menu_app.add_cascade(menu=opcionesMenu,label='Archivo')#tome las opciones del menu "opcionesMenu" y desplieguelas como cascada en la opcion
                                                               # etiquetada archivo del menu "menu_app"

    def _abrirArchivo(self):
        self.archivo_abierto=askopenfile(mode='r+')# abrira una ventana emergente que permitira seleccionar un archivo a abrir en  modo escritura-lectura
        self.editor_texto.delete(1.0,tk.END)#borrar el contenido de la caja de texto donde se visualizaran y editaran los archivos, esto con el fin de evitar que
                                            #algun texto escrito en este espacio sea agregado al documento abierto.
        if not self.archivo_abierto: # si se tiene un archivo abierto se retorna el control a la aplicacion
            return
        with open (self.archivo_abierto.name,'r+') as self.archivo : # abrir un archivo en modo escritura/lectura como un recurso para que el mismo se abra y se cierre de manera automatica
            texto=self.archivo.read()#leer la informacion del archivo
            self.editor_texto.insert(1.0,texto)#mostrar en la caja de texto el contenido leido del archivo
            self.title(f'{self.archivo.name}')#cambiar el titulo de la ventana para conocer que archivo se esta trabajando


    def _guardarArchivo(self):
        if self.archivo_abierto:# si se tiene un archivo abierto previamente implica que el mismo existe por lo cual no se debera
                                # crear uno nuevo si no sobreescribirlo
            with open(self.archivo_abierto.name,'w') as self.archivo: # archivo abierto en modo escritura, una vez finaliza el bloque with el
                                                                      # recurso el liberado de manera automatica
                texto=self.editor_texto.get(1.0,tk.END)# tomar todo el contenido de la caja de texto desde el inicio hasta el final
                self.archivo.write(texto)# se escribe sobre el archivo abierto la modificacion realizada
                self.title(f'{self.archivo.name}')

        else:
            self._guardarArchivoComo()# si no se tienen ningun archivo abierto se tiene que crear un nuevo archivo en el cual se almacenaran los datos

    def _guardarArchivoComo(self):
        self.archivo= asksaveasfilename(defaultextension='txt',filetype=[('Archivos de texto','*.txt'),('Todos los archivos','*.*')])#extension por defecto del archivo a guardad txt,
                                                                                                                                    #tipos de extensiones habilitadas para guardar mas no para leer
                                                                                                                                    #todas

        if not self.archivo:#si el archivo no guardo correctamente se regresa el control a la aplicacion
            return

        with open(self.archivo,'w') as self.archivo:#se abre el archivo que se acaba de crear
            texto=self.editor_texto.get(1.0,tk.END)# captura los datos del bloque de texto
            self.archivo.write(texto)#los datos capturados son escritos en el archivo creado anteriormente
            self.title(f'{self.archivo.name}')#se imprime en la ventana la direccion del archivo
            self.archivo_abierto=self.archivo# se le asigna al atributo archivo_abierto el objeto completo archivo, esto para evitar que al presionar el boton
                                            # guardar como y luego guardar se abra la ventana emergente para seleccionar el nombre del archivo deseado
                                            # y de forma automatica se le asigne el contenido leido del bloque de texto al archivo abierto actualmente