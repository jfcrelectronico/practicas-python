from conexionpull import conexion
from cursor_del_pool import cursorDelPool
from persona import persona
from logger_base import log
import psycopg2

class personaDAO:
    '''
    DAO-> DATA ACCESS OBJECT
    CRUD -> CREATE READ UPGRADE DELETE
    '''
    _SELECCIONAR='SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR='INSERT INTO persona(nombre, apellido, email) VALUES (%s,%s,%s)'
    _ACTUALIZAR='UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
    _DELETE='DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        #with conexion.obtenerConexion() as conexion_Actual: se usa cuando no se implementa un pool de conexiones
        with cursorDelPool() as cursor: #se llama la clase cursor del pool para generar la conexion y recibir el cursor
            cursor.execute(cls._SELECCIONAR)
            registros=cursor.fetchall()
            personas_lista=[]
            for registro in registros:
                personas=persona(registro[0],registro[1],registro[2],registro[3])#crea un objeto del tipo persona
                personas_lista.append(personas)
            return  personas_lista

    @classmethod
    def insertar(cls,persona_nueva):
        #with conexion.obtenerConexion():#abrir conexion se usa cuando no se implementa un pool de conexiones
            #with conexion.crear_cursor() as cursor:#abrir cursor se usa cuando no se implementa un pool de conexiones
        with cursorDelPool() as cursor:  # se llama la clase cursor del pool para generar la conexion y recibir el cursor
            valores=(persona_nueva.nombre,persona_nueva.apellido,persona_nueva.email)
            cursor.execute(cls._INSERTAR,valores)
            log.debug(f'registro a insertar: {persona_nueva}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, actualizar_persona):
        # with conexion.obtenerConexion() as conexion_Actual:
        #     with conexion_Actual.cursor() as cursor:
        with cursorDelPool() as cursor:  # se llama la clase cursor del pool para generar la conexion y recibir el cursor
            valores=(actualizar_persona.nombre,actualizar_persona.apellido,actualizar_persona.email,actualizar_persona.id_persona)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug(f'registro a actualizar: {actualizar_persona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, actualizar_persona):
        # with conexion.obtenerConexion() as conexion_Actual:
        #     with conexion_Actual.cursor() as cursor:
        with cursorDelPool() as cursor:  # se llama la clase cursor del pool para generar la conexion y recibir el cursor
            valores = actualizar_persona.id_persona,
            cursor.execute(cls._DELETE, valores)
            log.debug(f'registro a eliminar: {actualizar_persona}')
            return cursor.rowcount



if __name__=='__main__':
    #insertar una persona a la base de datos
    nuevo_registro = persona(nombre='vamos',apellido= 'full-stack',email= 'jfcrdevelopment@mail.com')
    insertados = personaDAO.insertar(nuevo_registro)
    log.debug(f'registros insertados: {insertados}')
    #
    #actualizar un registro en la base de datos
    actualizar_registro=persona(nombre='julian',apellido= 'carmona',email= 'jcarmona@mail.com',id_persona='35')
    actualizados = personaDAO.actualizar(actualizar_registro)
    log.debug(f'registros actualizados: {actualizados}')

    #borrar un registro de la base de datos
    borrar_registro=persona(id_persona=36)
    borrados=personaDAO.eliminar(borrar_registro)
    log.debug(f'el registro eliminado fue: {borrados}')

    #leer los registros de la base de datos
    leer=personaDAO.seleccionar()
    for personas in leer:
        log.debug(personas)#como personas es un objeto de la clase persona llama al metodo str cuando se imprime el debug

