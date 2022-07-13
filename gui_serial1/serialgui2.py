from tkinter import *
import serial.tools.list_ports
import threading
import signal

def signal_handler(signum,frame):
    sys.exit()

signal.signal(signal.SIGINT,signal_handler)

#class Graphics():
 #   pass


def connect_menu_init():
    global root,connect_btn,refresh_btn,graficaobj
    root=Tk()
    root.title("Celmed termohigrometro")
    root.geometry("500x500")
    root.config(bg='white')

    port_label = Label(root, text="Puertos Habilitados: ", bg='white')
    port_label.grid(row=2, column=0, pady=20, padx=10,sticky='w')

    port_bd=Label(root,text="Tasa de datos: ",bg='white')
    port_bd.grid(row=3,column=0,pady=20,padx=10,sticky='w')

    refresh_btn=Button(root,text='R',height=2,width=10,command=actualizar_puertos)
    refresh_btn.grid(row=2,column=2,pady=20,padx=10)

    connect_btn=Button(root,text='Conectar',height=2,width=10,state='disabled',command=conexion)
    connect_btn.grid(row=4,column=2,pady=20,padx=10)
    baud_select()
    actualizar_puertos()

    #graficaobj=Graphics()
    # graficaobj.canvas = Canvas(root, width=300, height=300, bg="white")
    # graficaobj.canvas.grid(row=5,columnspan=5)
    graficaobj=Canvas(root,width=300,height=300,bg="white",highlightthickness=0)
    graficaobj.grid(row=5,columnspan=5)
    #actualizacion  dinamica
    graficaobj.outer=graficaobj.create_arc(10,10,290,290,start=90,extent=100,outline='blue',fill='blue',width=2)

    #actualizacion estatica
    graficaobj.create_oval(75,75,225,225,outline='blue',fill='white',width=2)
    # actualizacion  dinamica
    graficaobj.text = graficaobj.create_text(150, 150, anchor=E, font=('Helvetica', '20'), text='---')
    #actualizacion  estatica
    graficaobj.text = graficaobj.create_text(150, 150, anchor=W, font=('Helvetica', '20'), text='und')
def baud_select():
    global  btn_presionado_br,drop_bd
    btn_presionado_br=StringVar()
    bds=["-",
         "300",
         "600",
         "1200",
         "2400",
         "4800",
         "9600",
         "14400",
         "19200",
         "28800",
         "38400",
         "56000",
         "57600",
         "115200",
         "128000",
         "256000"]

    btn_presionado_br.set(bds[0])
    drop_bd=OptionMenu(root,btn_presionado_br,*bds,command=verificar_conexion)
    drop_bd.config(width=20)
    drop_bd.grid(row=3,column=1,padx=50)

def actualizar_puertos():
    global puertos_presionado,drop_com
    ports=serial.tools.list_ports.comports()
    coms= [com[0] for com in ports]
    coms.insert(0,"-")

    try:
        drop_com.destroy()
    except:
        pass


    puertos_presionado=StringVar()
    puertos_presionado.set(coms[0])
    drop_com = OptionMenu(root, puertos_presionado, *coms,command=verificar_conexion)
    drop_com.config(width=20)
    drop_com.grid(row=2, column=1, padx=50)
    verificar_conexion(0)

def verificar_conexion(args):
    if "-" in puertos_presionado.get() or "-" in btn_presionado_br.get():
       connect_btn["state"]="disabled"
    else:
        connect_btn["state"]="active"

def conexion():
    global ser,datoserial
    if connect_btn["text"] in "Desconectar":
        datoserial = False
        connect_btn["text"]="Conectar"
        refresh_btn["state"]="active"
        drop_bd["state"]="active"
        drop_com["state"]="active"
        ser.close()
    else:
        datoserial = True
        connect_btn["text"]="Desconectar"
        refresh_btn["state"] = "disable"
        drop_bd["state"] = "disable"
        drop_com["state"] = "disable"
        port=puertos_presionado.get()
        baud=btn_presionado_br.get()

        #print(port,baud)
        try:
            ser=serial.Serial(port,baud)
        except:
            pass
        t1=threading.Thread(target=leer_dato_serial)
        t1.daemon=True
        t1.start()

def  leer_dato_serial():
    global datoserial,graficaobj
    while datoserial:
        dato= ser.readline()
        #print(type(dato))
        prueba=str(dato).strip("\\n").strip("\\r")
        prueba=prueba.split(",")
        #print(prueba)
        if len(prueba)>0:
            try:
                #print(prueba[0],type(prueba[0]))
                valor=int(prueba[0])
                print(f'valor actual {valor}')
                graficaobj.valor=valor
                t2=threading.Thread(target=control_grafica,args=(graficaobj,))
                t2.daemon=True
                t2.start()
            except:
                print('No se realiza proceso')
                pass

def control_grafica(graficaobj):
    graficaobj.itemconfig(graficaobj.outer, exten=int(graficaobj.valor))
    graficaobj.itemconfig(graficaobj.text, text=f'{int(graficaobj.valor)}')

def cerrar_ventana():
    global root,datoserial
    datoserial=False
    root.destroy()

connect_menu_init()
root.protocol("WM_DELETE_WINDOW",cerrar_ventana)
root.mainloop()