import tkinter as tk

class calculadora(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('400x450+400+200')
        self.title("Calculador")
        self.iconbitmap('calculadora.ico')
        self.resizable(0,0)
        #atributos de la clase
        self.expresion=''
        #pantalla de la calculadora
        self.entrada=None
        #se crea un stringvar para asociar luego la entrada a una variable y asi poderla evaluar
        self.operdig=tk.StringVar()
        self.subdivisiones()


    def subdivisiones(self):

        pantalla=tk.Frame(self,width=400,height=50,bg='grey')#un frame es un contenedor que permite alojar dentro otros widgets "componentes", para este caso alojara una entrada de texto
        pantalla.pack(side=tk.TOP)
        #definir la entrada para la pantalla
        entrada=tk.Entry(pantalla,font=('arial',18,'bold'),textvariable=self.operdig,width=30,justify=tk.RIGHT)
        entrada.grid(row=0,column=0,ipady=10)

        botones = tk.Frame(self, width=400, height=450, bg='grey')# se crea un objeto del tipo frame
        botones.pack()

        #region botones fila 1

        btnlimpiar=tk.Button(botones,text='C',width='32',height='3',bd=0,bg='#eee',cursor='hand2',command=self.eventolimpiar)
        btnlimpiar.grid(row=0,column=0,columnspan=3,padx=1,pady=1)

        btndivision = tk.Button(botones,text='/',width='10',height=3,bd=0,bg='#eee',cursor='hand2',command=lambda : self.concatenar(btndivision['text']))# a traves de lamda se asocia una funcion pero esta no es llamada
                                                                                                                                                        #si no hasta el momento en que se obtura el boton para este casp, si no se usa de esta manera
                                                                                                                                                        #solo en la creacion del boton la funcion es invocada
                                                                                                                                                        #a esto se le conoce como llamado de funciones anonimas
        btndivision.grid(row=0,column=3,padx=1,pady=1)

        #endregion
        #region botones fila 2
        btnuno= tk.Button(botones, text='1', width='10', height=3, bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self.concatenar(btnuno['text']))#cursor es la foma que tendra el puntero del mouse al posicionarse sobre un boton
        btnuno.grid(row=1, column=0, padx=1, pady=1)

        btndos = tk.Button(botones, text='2', width='10', height=3, bd=0, bg='#fff', cursor='hand2',
                           command=lambda: self.concatenar(btndos['text']))
        btndos.grid(row=1, column=1, padx=1, pady=1)

        btntres = tk.Button(botones, text='3', width='10', height=3, bd=0, bg='#fff', cursor='hand2',
                           command=lambda: self.concatenar(btntres['text']))
        btntres.grid(row=1, column=2, padx=1, pady=1)

        btnsuma = tk.Button(botones, text='+', width='10', height=3, bd=0, bg='#eee', cursor='hand2',
                           command=lambda: self.concatenar(btnsuma['text']))
        btnsuma.grid(row=1, column=3, padx=1, pady=1)
        #endregion
        #botones fila 3
        btncuatro = tk.Button(botones, text='4', width='10', height=3, bd=0, bg='#fff', cursor='hand2',
                           command=lambda: self.concatenar(btncuatro['text']))
        btncuatro.grid(row=2, column=0, padx=1, pady=1)

        btncinco = tk.Button(botones, text='5', width='10', height=3, bd=0, bg='#fff', cursor='hand2',
                           command=lambda: self.concatenar(btncinco['text']))
        btncinco.grid(row=2, column=1, padx=1, pady=1)

        btnseis = tk.Button(botones, text='6', width='10', height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self.concatenar(btnseis['text']))
        btnseis.grid(row=2, column=2, padx=1, pady=1)

        btnresta = tk.Button(botones, text='-', width='10', height=3, bd=0, bg='#eee', cursor='hand2',
                            command=lambda: self.concatenar(btnresta['text']))
        btnresta.grid(row=2, column=3, padx=1, pady=1)
        # endregion
        # botones fila 4
        btnsiete = tk.Button(botones, text='7', width='10', height=3, bd=0, bg='#fff', cursor='hand2',
                              command=lambda: self.concatenar(btnsiete['text']))
        btnsiete.grid(row=3, column=0, padx=1, pady=1)

        btnocho = tk.Button(botones, text='8', width='10', height=3, bd=0, bg='#fff', cursor='hand2',
                             command=lambda: self.concatenar(btnocho['text']))
        btnocho.grid(row=3, column=1, padx=1, pady=1)

        btnnueve = tk.Button(botones, text='9', width='10', height=3, bd=0, bg='#fff', cursor='hand2',
                            command=lambda: self.concatenar(btnnueve['text']))
        btnnueve.grid(row=3, column=2, padx=1, pady=1)

        btnmultiplicacion = tk.Button(botones, text='*', width='10', height=3, bd=0, bg='#eee', cursor='hand2',
                             command=lambda: self.concatenar(btnmultiplicacion['text']))
        btnmultiplicacion.grid(row=3, column=3, padx=1, pady=1)
        # endregion
        # botones fila 5
        btncero = tk.Button(botones, text='0', width='21', height=3, bd=0, bg='#fff', cursor='hand2',
                             command=lambda: self.concatenar(btncero['text']))
        btncero.grid(row=4,column=0, columnspan=2, padx=1, pady=1)

        btnpunto = tk.Button(botones, text='.', width='10', height=3, bd=0, bg='#eee', cursor='hand2',
                            command=lambda: self.concatenar(btnpunto['text']))
        btnpunto.grid(row=4, column=2, padx=1, pady=1)

        btnigual = tk.Button(botones, text='=', width='10', height=3, bd=0, bg='#eee', cursor='hand2',
                             command=self.evaluar)
        btnigual.grid(row=4, column=3, padx=1, pady=1)



    def eventolimpiar(self):
        self.expresion=''
        self.operdig.set(self.expresion)
    def concatenar(self,valor):
        self.expresion=f'{self.expresion}{valor}'#concatenar el valor de la variable expresion y con el nuevo valor ingresado
        self.operdig.set(self.expresion)
    def evaluar(self):
        try:
            if self.expresion:
                resultado=eval(self.expresion)# la funcion eval permite tomar una cadena de texto que contenga valores aritmeticos y ejecuta la operacion respectiva
                self.operdig.set(resultado)
        except:
            self.operdig.set("Error")
        finally:
            self.expresion = ''

