import psycopg2
import clave
#https://www.datacamp.com/community/tutorials/understanding-logistic-regression-python
#https://realpython.com/logistic-regression-python/


#https://towardsdatascience.com/building-a-logistic-regression-in-python-step-by-step-becd4d56c9c8
#https://towardsdatascience.com/logistic-regression-a-simplified-approach-using-python-c4bc81a87c31

# import pandas as pd
#
# #cabeceras =['pH','pCO2(mmHg)','pO2(mmHg)','cHCO3-(mmol/L)','BE(ecf)(mmol/L)','cSO2','Na+(mmol/L)','K+(mmol/L)','Ca++(mmol/L)','Cl-(mmol/L)','cTCO2(mmol/L)','AGap(mmol/L)','AGapk(mmol/L)','GLUCOSA(mg/dL)','LACTATO(mmol/L)','RESULTADO']
#
#
# datos = pd.read_csv('prueba2.csv',sep=';')
#
# # for i in datos.keys():
# #     print(i)
#
#
# tabla_variables_dependientes=['pH','pCO2 (mmHg)','pO2 (mmHg)','cHCO3- (mmol/L)','BE(ecf) (mmol/L)','cSO2','Na+ (mmol/L)','K+ (mmol/L)','Ca++ (mmol/L)','Cl- (mmol/L)','cTCO2 (mmol/L)','AGap (mmol/L)','AGapk (mmol/L)','GLUCOSA (mg/dL)','LACTATO (mmol/L)']
# # #
# # #
# X=datos[tabla_variables_dependientes]
# y=datos.RESULTADO
# #
# from sklearn.model_selection import train_test_split
#
# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

# #print(X_train)
# #print(y_train)
#
# from sklearn.linear_model import LogisticRegression
#
# logreg = LogisticRegression()
#
# # # fit the model with data
# logreg.fit(X_train,y_train)
# #
# # #
# y_pred=logreg.predict(X_test)
# #
# # # from sklearn import metrics
# # # cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
# # # cnf_matrix













# # # #la variable recibira el objeto generado por el metodo connect este metodo recibe un diccionario del tipo **kwargs
# conexion=psycopg2.connect(user='postgres',password=clave.clave,host='localhost',port='5432',database='test_db')
#
# #print(conexion)#para verificar si la conexion fue establecida con la base de datos
#
# #creamos un cursor es un objeto que permite ejecutar sentencias sql en postgres enviadas desde python
#
# cursor=conexion.cursor()
# sentencia='SELECT * FROM persona ORDER BY id_persona'
# cursor.execute(sentencia)#envia la sentencia como un query a la base de datos
# registros=cursor.fetchall()#permite recuperar TODOS los registros retornados luego de ejercutar el query enviado, llega una lista llena de tuplas
#
# print(registros)
#
# cursor.close()#cierra el objeto cursor
# conexion.close()#cierra el objeto conexion al igual que se hace con los archivos


# try:
#
#     with psycopg2.connect(user='postgres',password=clave.clave,host='localhost',port='5432',database='test_db') as conexion:
#         with conexion.cursor() as cursor: # cierra la conexion  al cursor de forma automatica
#             sentencia = 'SELECT * FROM persona WHERE id_persona=%s'#%s es un placeholder una variable
#             id_persona=[1]
#             cursor.execute(sentencia,tuple(id_persona))#el parametro que se le asigna al placeholder debe ser del tipo TUPLA
#             registros = cursor.fetchone()#solo recupera UN registro que esta limitado por la condicion establecida en la condicion WHERE,ahora registro ya no es una listra de tuplas si no una tupla unica
#             print(registros)
# except Exception as e:
#     print(f'Ocurrio un error de tipo: {e}')
#
# finally:
#     conexion.close()#cierra el objeto conexion al igual que se hace con los archivos

# try:
#
#     with psycopg2.connect(user='postgres',password=clave.clave,host='localhost',port='5432',database='test_db') as conexion:
#         with conexion.cursor() as cursor: # cierra la conexion  al cursor de forma automatica
#             sentencia = 'SELECT * FROM persona WHERE id_persona IN (%s,%s)'#%s es un placeholder una variable, la palabra reservada IN permite establecer la busqueda de multiples parametros
#             id_persona=[1,2]
#             cursor.execute(sentencia,tuple(id_persona))#el parametro que se le asigna al placeholder debe ser del tipo TUPLA
#             registros = cursor.fetchall()#recupera TODOS los registro que estan limitados por la condicion establecida en la condicion WHERE,ahora registro ya no es una lista de tuplas si no con las tupla correspondientes a cada condicional
#             print(registros)
# except Exception as e:
#     print(f'Ocurrio un error de tipo: {e}')
#
# finally:
#     conexion.close()#cierra el objeto conexion al igual que se hace con los archivos

# try:
#
#     with psycopg2.connect(user='postgres',password=clave.clave,host='localhost',port='5432',database='test_db') as conexion:
#         with conexion.cursor() as cursor: # cierra la conexion  al cursor de forma automatica
#             sentencia ='INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
#             valores=('jana','ruiz','jruiz@mail.com')
#             cursor.execute(sentencia,valores)
#             #conexion.commit()#como se esta modificando la base de datos el metodo commit permite guardar los valores en la misma, ahora como se esta realizando el acceso a la base de datos con with el commit se ejecuta de manera automatica
#             reg_insertados=cursor.rowcount#permite conocer la cantidad de registros insertados en el proceso
#             print(reg_insertados)
# except Exception as e:
#     print(f'Ocurrio un error de tipo: {e}')
#
# finally:
#     conexion.close()#cierra el objeto conexion al igual que se hace con los archivos

# try:
#
#     with psycopg2.connect(user='postgres',password=clave.clave,host='localhost',port='5432',database='test_db') as conexion:
#         with conexion.cursor() as cursor: # cierra la conexion  al cursor de forma automatica
#             sentencia ='INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
#             valores=(('albert','daza','adaza@mail.com'),('claudia','daza','cdaza@mail.com'),('maria','medina','mmedina@mail.com'))
#             cursor.executemany(sentencia,valores)#permite insertar multiples registros en simultanea
#             #conexion.commit()#como se esta modificando la base de datos el metodo commit permite guardar los valores en la misma, ahora como se esta realizando el acceso a la base de datos con with el commit se ejecuta de manera automatica
#             # reg_insertados=cursor.rowcount#permite conocer la cantidad de registros insertados en el proceso
#             # print(reg_insertados)
# except Exception as e:
#     print(f'Ocurrio un error de tipo: {e}')
#
# finally:
#     conexion.close()#cierra el objeto conexion al igual que se hace con los archivos

# try:
#
#     with psycopg2.connect(user='postgres',password=clave.clave,host='localhost',port='5432',database='test_db') as conexion:
#         with conexion.cursor() as cursor: # cierra la conexion  al cursor de forma automatica
#             sentencia ='UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
#             valores=(('julio','daza','jdaza@mail.com','8'),('estrella','medina','emedina@mail.com','9'),('andrea','rodriguez','erodriguez@mail.com','10'))
#             cursor.executemany(sentencia,valores)#permite insertar multiples registros en simultanea
#             #conexion.commit()#como se esta modificando la base de datos el metodo commit permite guardar los valores en la misma, ahora como se esta realizando el acceso a la base de datos con with el commit se ejecuta de manera automatica
#             # reg_actualizados=cursor.rowcount#permite conocer la cantidad de registros insertados en el proceso
#             # print(reg_actualizados)
# except Exception as e:
#     print(f'Ocurrio un error de tipo: {e}')
#
# finally:
#     conexion.close()#cierra el objeto conexion al igual que se hace con los archivos



# try:
#
#     with psycopg2.connect(user='postgres',password=clave.clave,host='localhost',port='5432',database='test_db') as conexion:
#         with conexion.cursor() as cursor: # cierra la conexion  al cursor de forma automatica
#             sentencia ='DELETE FROM persona WHERE id_persona=%s' #eliminar un unico registro
#             valores=8,
#             cursor.execute(sentencia,valores)#permite insertar multiples registros en simultanea
#             #conexion.commit()#como se esta modificando la base de datos el metodo commit permite guardar los valores en la misma, ahora como se esta realizando el acceso a la base de datos con with el commit se ejecuta de manera automatica
#             reg_eliminados=cursor.rowcount#permite conocer la cantidad de registros insertados en el proceso
#             print(reg_eliminados)
# except Exception as e:
#     print(f'Ocurrio un error de tipo: {e}')
#
# finally:
#     conexion.close()#cierra el objeto conexion al igual que se hace con los archivos

try:

    with psycopg2.connect(user='postgres',password=clave.clave,host='localhost',port='5432',database='test_db') as conexion:
        with conexion.cursor() as cursor: # cierra la conexion  al cursor de forma automatica
            sentencia ='DELETE FROM persona WHERE id_persona IN %s' # eliminar multiples registros
            #entrada=input("ingrese los  id de los registros a elmininar separados por comas")
            #valores=(tuple(entrada.split(',')),)
            valores2=(('7','9','10'),)
            #print(valores)
            #print(valores2)
            cursor.execute(sentencia,valores2)#permite insertar 1 registro
            #conexion.commit()#como se esta modificando la base de datos el metodo commit permite guardar los valores en la misma, ahora como se esta realizando el acceso a la base de datos con with el commit se ejecuta de manera automatica
            reg_eliminados=cursor.rowcount#permite conocer la cantidad de registros insertados en el proceso
            print(reg_eliminados)
except Exception as e:
    print(f'Ocurrio un error de tipo: {e}')

finally:
    conexion.close()#cierra el objeto conexion al igual que se hace con los archivos