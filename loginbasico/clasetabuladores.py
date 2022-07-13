import tkinter as tk
from tkinter import ttk,messagebox,scrolledtext
import time


class tabuladores(tk.Tk):# Heredar de la clase padre el constructor

    def __init__(self):
        super().__init__()#siempre se inicializan primero las clases padre
        self.geometry('600x400+400+200')  # 600x 400 indica el tamaño de la ventana, mientras +400+200 la posicion en pantalla en la cual se desplegara la ventana inicialmente
        self.title('componentes')
        self.iconbitmap('icono.ico')
        #self.crear_tabuladores()

    def crear_tabuladores(self):#self hace referencia al componente mismo para este caso cuando se crea un objeto como este hereda de la clase tk la cual creara una ventana
        #creando un tabcontrol con la clase notebook, este espera recibir el objeto de tipo ventana para este tipo de programacion seria el parametro self osea "el mismo objeto"
        control_tabulador = ttk.Notebook(self)#control_tabulador pertenece al widget ventana
        #agregando un frame esto permite agregar componentes dentro de cada tabulador
        tabulador1 = ttk.Frame(control_tabulador)#un frame es un contenedor que permite alojar otros widgets "componentes"
        #agregar tabulador1 al control de tabuladores
        control_tabulador.add(tabulador1,text='Tabulador 1')
        #el metodo pack empaqueta un componente "widget" en el paquete padre para este caso el paquete padre es ventana
        control_tabulador.pack(fill='both')#pack permite ubicar dentro de un contenedor los widgets en ubicaciones especificas e indicarles en su posicion cuanto
                                           #espacio deben llenar, es similar a grid pero este tiene limitaciones en ciertas propiedades
        tabulador2=ttk.LabelFrame(control_tabulador,text='Tabulador2')#labelFrame permite crear un contenedor y ademas ponerle una etiqueta a dicho contenedor
        control_tabulador.add(tabulador2,text='Tabulador2')

        tabulador3 = ttk.LabelFrame(control_tabulador,
                                    text='Tabulador3')  # labelFrame permite crear un contenedor y ademas ponerle una etiqueta a dicho contenedor
        control_tabulador.add(tabulador3, text='Tabulador3')

        tabulador4 = ttk.LabelFrame(control_tabulador,
                                    text='Tabulador4')  # labelFrame permite crear un contenedor y ademas ponerle una etiqueta a dicho contenedor
        control_tabulador.add(tabulador4, text='Tabulador4')

        tabulador5 = ttk.LabelFrame(control_tabulador,
                                    text='Tabulador5')  # labelFrame permite crear un contenedor y ademas ponerle una etiqueta a dicho contenedor
        control_tabulador.add(tabulador5, text='Tabulador5')


        self._componentes_tabulador1(tabulador1)
        self._componentes_tabulador2(tabulador2)
        self._componentes_tabulador3(tabulador3)
        self._componentes_tabulador4(tabulador4)
        self._componentes_tabulador5(tabulador5)

    def _componentes_tabulador1(self,tabulador):
        etiqueta1 = ttk.Label(tabulador, text='Entrada1')
        etiqueta1.grid(row=0, column=0, padx=2, pady=2)
        entrada1 = ttk.Entry(tabulador, width=50)
        entrada1.grid(row=0, column=1, padx=2, pady=2)
        etiqueta2 = ttk.Label(tabulador, text='Boton1')
        etiqueta2.grid(row=1, column=0, padx=2, pady=2)
        def _mensaje():
            messagebox.showinfo('Mensaje',f'Se presiono el boton el valor digitado en la entrada de texto es {entrada1.get()}')
        boton1 = ttk.Button(tabulador, text='Boton 1', command=_mensaje)
        boton1.grid(row=1, column=1, sticky='w')
    def _componentes_tabulador2(self,tabulador):
        barravertical=scrolledtext.ScrolledText(tabulador,width=15,height=4,wrap=tk.WORD)# se crea un  nuevo objeto del tipo ScrolledText, width especifica el ancho de la ventana de texto en caracteres
                                                                        #height especifica el alto del cuadro de texto en caracteres
                                                                        #la propiedad wrap permite que al llegar al final del limite de escritura en el cuadro de texto
                                                                        #las palabras sean separadas completas y no por partes
        # barravertical.insert(tk.INSERT,"VALOR POR DEFECTO")#agregar un valor por defecto al cuadro de texto
        barravertical.grid(row=0,column=0)
    def _componentes_tabulador3(self,tabulador):
        valores=[x+1 for x in range(10)]#en pyhton esta estrucutura es dnominada un list comprehension
        datalist=ttk.Combobox(tabulador,width=5,values=valores)#cargar el objeto data list de tipo combobox con los valores del arreglo
        datalist.grid(row=0,column=0)
        datalist.insert(0,'-')# inserta en la posicion deseada un caracter indicado
        datalist.current(4)#especifica la posicion deseada de los valores que hacen parte del combobox y sera mostrada por defecto al desplegar la interface

    def _componentes_tabulador4(self,tabulador):
        imagen1=tk.PhotoImage(file='icono.png')
        def _informacion():
            messagebox.showinfo('ruta imagen',f'{imagen1.cget("file")}')
        boton_imagen=ttk.Button(tabulador,image=imagen1,command=_informacion)
        boton_imagen.grid(row=0, column=0)

    def _componentes_tabulador5(self,tabulador):
        barra_progreso=ttk.Progressbar(tabulador,orient='horizontal',length=500)#orient indica la orientacion que se desea para la barra, la longitud esta dada en pixeles
        barra_progreso.grid(row=0,column=0,columnspan=2)#el valor asigando a colum span depende de lña longitud de la barra

        #barra_progreso.step(1.5)#incrementa el progreso de la carga de la barra en un valor determinado

        def _detener(self):
            self.after(2000, barra_progreso.stop)#detiende la ejecucion del progreso de la barra despues de 2000ms
        def _iniciar(self):
            barra_progreso.start()  # inicia animacion de carga de la barra de progreso
        def _StepbyStep(self):
            barra_progreso['maximum']=100 # a la propiedad maximo de la barra de progreso asigenele 100
            for i in range(101):
                time.sleep(0.3)
                barra_progreso['value']=i# en la propiedad value de la barra progreso asigne el valor de la variable i
                barra_progreso.update()#actualizar el valor de la barra de progreso
                #label_barra['text'] = barra_progreso['value']#mostrar el un label el valor actual de la barra de progreso
            barra_progreso['value']=0# asignar a la barra de progreso el valor de 0 luego de terminar la ejecucion del ciclo de carga

        boton_iniciar = tk.Button(tabulador, text='Iniciar Progreso', command=_iniciar)
        boton_iniciar.grid(row=1, column=0)
        boton_detener=tk.Button(tabulador,text='Detener Progreso',command=_detener)
        boton_detener.grid(row=1,column=1)
        boton_incrementarstep = tk.Button(tabulador, text='Step-by-Step Progreso', command=_StepbyStep)
        boton_incrementarstep.grid(row=1, column=2)
        label_barra=tk.Label(tabulador,text='--')
        label_barra.grid(row=2,column=1)

