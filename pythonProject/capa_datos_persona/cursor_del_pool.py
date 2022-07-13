from logger_base import log
from conexionpull import conexion
class cursorDelPool:

    def __init__(self):
        self._conexion=None
        self._cursor=None

#Using these magic methods (__enter__, __exit__) allows you to implement objects which can be used easily with the with statement.

#The idea is that it makes it easy to build code which needs some 'cleandown' code executed (think of it as a try-finally block)


    ###este seria el bloque try
    def __enter__(self):
        log.debug('Inicio del metodo with __enter__')
        self._conexion=conexion.obtenerConexion()#crea el objeto a partir de metodo obtener conexion
        self._cursor=self._conexion.cursor()#crear el cursor para la conexion obtenida
        return  self._cursor # el objeto sera el encargado de consultar la base de datos
    ### este seria el bloque finally
    def __exit__(self,tipo_de_excepcion,valor_expcion,detalle_excepcion):
        log.debug('Se ejecuta metodo exit')
        if valor_expcion:# si exite algo cargado en el parametro implica que se genero un excepcion y se debe hacer un rollback de la transferencia
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion: {valor_expcion}{tipo_de_excepcion}{detalle_excepcion}')
        else:
            self._conexion.commit()
            log.debug('commit de la transaccion')
        self._cursor.close()#cierra el cursor
        conexion.liberar_conexion(self._conexion)#liberar los recursos del pool

if __name__ =='__main__':
    #el uso de la sentencia with hace referencia a apliacion de resource manager
      with cursorDelPool() as cursor:
          log.debug('Dentro del bloque with')
          cursor.execute('SELECT * FROM persona')
          log.debug(cursor.fetchall())


