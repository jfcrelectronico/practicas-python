import psycopg2
import clave

# conexion= psycopg2.connect(user='postgres',password=clave.clave,host='localhost',port='5432',database='test_db')
# try:
#
#  #como no se usa un bloque with no se hace un commit (actualizacion) automaticamente del query a la base de datos
#
#     conexion.autocommit = False# el valor por defecto es False, esto permite que si se genero un error en un query no se guarden los cambios
#     cursor=conexion.cursor() # cierra la conexion  al cursor de forma automatica
#     # sentencia ='INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)' # eliminar multiples registros
#     # #entrada=input("ingrese los  id de los registros a elmininar separados por comas")
#     # #valores=(tuple(entrada.split(',')),)
#     # valores2=('Cristian','Ruiz','cruiz@mail.com')
#     # #print(valores)
#     # #print(valores2)
#     # cursor.execute(sentencia,valores2)
#
#     sentencia='UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
#     valores2=('Vicente','Rodriguez','vrodriguez@mail.com',11)
#     cursor.execute(sentencia,valores2)
#
#     # sentencia = 'DELETE FROM persona WHERE id_persona=23'
#     # valores2 = ('Vicente', 'Rodriguez', 'vrodriguez@mail.com', 11)
#     # cursor.execute(sentencia)
#
#     #conexion.commit()#como se esta modificando la base de datos el metodo commit permite guardar los valores en la misma, ahora como se esta realizando el acceso a la base de datos con with el commit se ejecuta de manera automatica
#     #reg_eliminados=cursor.rowcount#permite conocer la cantidad de registros insertados en el proceso
#     #print(reg_eliminados)
#     conexion.commit()#permite que se haga la actualizacion del query respectivo
# except Exception as e:
#     conexion.rollback()
#     print(f'Ocurrio un error de tipo,se genero un rollback {e}')
#
# finally:
#     conexion.close()#cierra el objeto conexion al igual que se hace con los archivos

try:

    with psycopg2.connect(user='postgres',password=clave.clave,host='localhost',port='5432',database='test_db') as conexion:
        with conexion.cursor() as cursor: # cierra la conexion  al cursor de forma automatica
            sentencia = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
            valores2=('Vicente','Rodriguez','vrodriguez@mail.com',11)
            cursor.execute(sentencia,valores2)

            sentencia = 'DELETE FROM persona WHERE id_persona=5'
            cursor.execute(sentencia)

            #conexion.commit()#como se esta modificando usando wl metodo with este de manera automatica genera un commit si el query no presenta ningun error
            # reg_eliminados=cursor.rowcount#permite conocer la cantidad de registros insertados en el proceso
            # print(reg_eliminados)
except Exception as e:
    print(f'Ocurrio un error de tipo:se genero un rollback {e}')

finally:
    conexion.close()#cierra el objeto conexion al igual que se hace con los archivos