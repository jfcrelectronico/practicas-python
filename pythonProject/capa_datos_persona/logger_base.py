import logging as log


# dependiendo del nivel seleccionado se desplagaran los mensajes de log
#siendo el nivel de debug el que los implica a todos, si se selecciona un nivel
#inferior sus niveles superiores no seran mostrados

#datefmt-> formato de la hora HORA, MINUTO SEGUNDO y p IMPLICA SI ES AM O PM
#crea un archivo con extension .log donde se almacenaran los datos de los mensajes de loggin
#log.StreamHandler-> es la consola del pycharm

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capadatos.log'),
                    log.StreamHandler()
                ]
                )

if __name__=='__main__':
    log.debug('mensaje a nivel de debug')
    log.info('mensaje a nivel de info')
    log.warning('mensaje a nivel de warning')
    log.error('mensaje a nivel de error')
    log.critical('mensaje a nivel de critical')




