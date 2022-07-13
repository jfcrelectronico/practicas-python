#a diferencia de una conexion simple el pool de conexiones permite que multiples usuarios accedan a la base de datos
#en "simultanea"

from logger_base import log
from psycopg2 import pool
import sys
class conexion:
    _database='test_db'
    _username='postgres'
    _password='@Jfcr2010'
    _db_port='5432'
    _host='localhost'
    _MIN_CON=1
    _MAX_CON=5
    _pool=None


    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool=pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON,
                                                    host=cls._host,
                                                    user=cls._username,
                                                    password=cls._password,
                                                    port=cls._db_port,
                                                    database=cls._database
                                                    )#crear una conexion a la base de datos del tipo pool
                log.debug(f'Creacion de pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'ocrurrio un error {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        establecer_conexion=cls.obtenerPool().getconn()#retorna UN objeto de conexion hacia la base de datos del pool creado
        log.debug(f'conexion obtenida de pool : {establecer_conexion}')
        return establecer_conexion

    #retornar recursos al pool de conexiones
    @classmethod
    def liberar_conexion(cls,objeto):
        cls.obtenerPool().putconn(objeto)#retorna la conexion al pool de conexiones
        log.debug(f'regresamos el objeto conexion: {objeto}')

    #cerrar el objeto de pool de conexiones
    @classmethod
    def cerrar_conexiones(cls):
        cls.obtenerPool().closeall()#cierra todos los objetos de conexion del pool




if __name__=='__main__':

    conexion1=conexion.obtenerConexion()
    # cuando se termina de usar un objeto el mismo libera lo recuersos los cuales regresan al pool para ser usados por otro cliente
    conexion.liberar_conexion(conexion1)
    conexion2=conexion.obtenerConexion()
    conexion3 = conexion.obtenerConexion()
    conexion4 = conexion.obtenerConexion()
    conexion5 = conexion.obtenerConexion()
    # a pesar de limitar el pool a 5 conexiones como se libero la conexion 1 se vuelve a habilitar el recurso
    conexion6 = conexion.obtenerConexion()
