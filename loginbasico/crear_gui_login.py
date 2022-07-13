import tkinter as tk
from tkinter import ttk,messagebox
logo='C:/proyectos_python/loginbasico/logo/IOTHIX-LIGHT-firma.ico'#ruta del logo que tendra la ventana

class login_gui(tk.Tk):#heradamos de la clase tk

    def __init__(self):
        super().__init__()#inicializacion de la clase padre
        self.geometry('300x130')  # tamaño ventana (ancho x alto)
        self.title('Iothix')  # titulo de la ventana
        self.iconbitmap(logo)  # agregar logo a la ventana
        self.resizable(0, 0)  # evitar que la ventana sea maximizada
        # configurar ancho de filas y columnas
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self._crear_componentes()#llamado a metodo protegido solo se puede llamar desde la clase

    def _crear_componentes(self):
        # crear etiquetas para entrada de texto
        lbl_usuario = ttk.Label(self, text='Usuario: ')
        lbl_usuario.grid(row=0, column=0, pady=5, padx=5, sticky="E")

        lbl_clave = ttk.Label(self, text='Clave: ')
        lbl_clave.grid(row=1, column=0, pady=5, padx=5, sticky="E")
        # variables clase, para entradas de texto
        self.var_usuario = tk.StringVar()
        self.var_clave = tk.StringVar()


        # crear entrada de texto
        usuario = ttk.Entry(self, textvariable=self.var_usuario)
        usuario.grid(row=0, column=1, pady=5, padx=5, sticky="W")

        clave = ttk.Entry(self, textvariable=self.var_clave, show="*")
        clave.grid(row=1, column=1, pady=5, padx=5, sticky="W")

        # crear boton
        btn_login = ttk.Button(self, text='Login', command=self._capturar)
        btn_login.grid(row=3, column=0, columnspan=2, pady=5, padx=5)

    def _capturar(self):
        messagebox.showinfo('Valores digitados', f'usuario: {self.var_usuario.get()} \nclave: {self.var_clave.get()}')









