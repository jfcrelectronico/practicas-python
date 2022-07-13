from logger_base import log
import psycopg2 as ps
import sys
class conexion:
    _database='test_db'
    _username='postgres'
    _password='@Jfcr2010'
    _db_port='5432'
    _host='localhost'
    _conexion=None
    _cursor=None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion=ps.connect(user=cls._username,password=cls._password,host=cls._host,port=cls._db_port,database=cls._database)
                log.debug(f'conexion exitosa: {cls._conexion}')
                return cls._conexion

            except Exception as e:
                log.error(f'Ocurrio una excepcion al obtener la conexion: {e}')
                sys.exit()#termina por completo el programa
        else:
            return cls._conexion

    @classmethod
    def crear_cursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor= cls.obtenerConexion().cursor()# se invoca el metodo obtener conexion si es efectivo se solicita el objeto cursor

                log.debug(f'se abrio correctamente el cursor: {cls._cursor}')
                return cls._cursor

            except Exception as e:
                log.error(f'Ocurrio una excepcion al obtener el cursor: {e}')
                sys.exit()  # termina por completo el programa
        else:
            return cls._cursor


if __name__=='__main__':
    conexion.obtenerConexion()
    conexion.crear_cursor()
