from tkinter import *
import serial.tools.list_ports
import functools

ports= serial.tools.list_ports.comports()
serialObj=serial.Serial()

root=Tk()
root.config(bg='grey')


def closeComPort(indexport):
    indexport.close()

def initComPort(index):
    currentPort=str(ports[index])
    comPortVar=str(currentPort.split(' ')[0])
    #(print(comPortVar)
    serialObj.port=comPortVar
    serialObj.baudrate=115200
    serialObj.open()
    cerrar_puerto = Button(root, text='ClosePort', font=('Calibri', '11'), height=1, width=45)#,command=functools.partial(closeComPort, indexport=ports.index(comPortVar)))
    cerrar_puerto.grid(row=5, column=0)

for onePort in ports:
    comButton=Button(root,text=onePort,font=('Calibri','11'),height=1,width=45,command=functools.partial(initComPort,index=ports.index(onePort)))
    comButton.grid(row=ports.index(onePort),column=0)

dataCanvas=Canvas(root,width=600,height=420,bg='white')
dataCanvas.grid(row=0,column=1,rowspan=100)





vsb=Scrollbar(root,orient='vertical',command=dataCanvas.yview)
vsb.grid(row=0,column=2,rowspan=100,sticky='ns')

dataCanvas.config(yscrollcommand=vsb.set)
dataFrame=Frame(dataCanvas,bg='white')
dataCanvas.create_window((10,0),window=dataFrame,anchor='nw')

def checkSerialPort():
    #dataCanvas.config(scrollregion=dataCanvas.bbox("all"))
    if serialObj.isOpen() and serialObj.in_waiting:
        recentPacket=serialObj.readline()
        #recentPacketString=recentPacket.decode('utf').rstrip('\n')
        Label(dataFrame,text=recentPacket,font=('Calibri','13'),bg='white').pack()

#checkSerialPort()


##root.mainloop()


while True:
    root.update()
    checkSerialPort()
    dataCanvas.config(scrollregion=dataCanvas.bbox("all"))