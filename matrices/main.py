# separar_matriz1=[]
# separar_matriz2=[]
# matriz_resultado=[]
#
#
# recibir_matriz1_string=input("ingrese la matriz separando las filas por comas y sin espacios entre los elementos: \n")
# contar_filas_m1=0
# contar_columnas_m1=recibir_matriz1_string.index(";")
#
# recibir_matriz2_string=input("ingrese la matriz separando las filas por comas y sin espacios entre los elementos: \n")
# contar_filas_m2=0
# contar_columnas_m2=recibir_matriz2_string.index(";")
#
# matriz1=recibir_matriz1_string.split(';')
# contar_filas_m1=len(matriz1)
# matriz2 = recibir_matriz2_string.split(';')
# contar_filas_m2=len(matriz2)
#
#
# if contar_columnas_m1==contar_filas_m2:
#     print("se puede realizar la multiplicacion")
#     print(f'Las dimensiones de la primer matriz son: {contar_filas_m1}X{contar_columnas_m1}')
#     print(f'Las dimensiones de la segunda matriz son: {contar_filas_m2}X{contar_columnas_m2}')
#
#
#     for elementos in matriz1:
#         respaldo=list(elementos)
#         for posicion in range(len(respaldo)):
#             separar_matriz1.append(respaldo[posicion])
#     #
#     # for elementos in matriz2:
#     #     respaldo2=list(elementos)
#     #     for posicion in range(len(respaldo2)):
#     #         separar_matriz2.append(respaldo2[posicion])
#     #
#     # print(separar_matriz1,'\n',separar_matriz2)
#
#     # control=len(separar_matriz1)//contar_filas_m1
#     # base=0
#     # valor=0
#     # for recorre_m1 in range(contar_columnas_m1):
#     #     valor=0
#     #     for recorre_m2 in range(contar_filas_m2):
#     #         valor+=int(separar_matriz1[base+recorre_m2])*int(separar_matriz2[recorre_m2])
#     #     base+=contar_columnas_m1
#     #     matriz_resultado.append(valor)
#     # print(matriz_resultado)
#
# else:
#     print("la multiplicacion no se puede realizar pues el orden de las matrices no concuerda")
#     print(f'Las dimensiones de la primer matriz son: {contar_filas_m1}X{contar_columnas_m1}')
#     print(f'Las dimensiones de la segunda matriz son: {contar_filas_m2}X{contar_columnas_m2}')

# Program to multiply two matrices using nested loops
#
# # 3x3 matrix
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# # 3x4 matrix
# Y = [[5,8,1,2],
#     [6,7,3,0],
#     [4,5,9,1]]
# # result is 3x4
# result = [[0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0]]
#
# # iterate through rows of X
# for i in range(len(X)):
#    # iterate through columns of Y
#    for j in range(len(Y[0])):
#        # iterate through rows of Y
#        for k in range(len(Y)):
#            result[i][j] += X[i][k] * Y[k][j]
#
# for r in result:
#    print(r)

class prueba:
    variable_prueba="jfcr"
    def __init__(self,mensaje):
        self.mensaje=mensaje
        print(self.mensaje)

    @property
    def respaldo(self):
        return self.mensaje

    @respaldo.setter
    def respaldo(self,cambiar):
        self.mensaje=cambiar
    @staticmethod
    def metodo_estatico():
        print(prueba.variable_prueba)##no permite interactuar con los atributos de los metodos solo con los
                                    ##atributos de las clases, para accesar a un atributo clase se debe especificar
                                    ##el nombre de la clase
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_prueba)##no permite interactuar con los atributos de los metodos solo con los
                                    ##atributos de las clases, para accesar a un atributo clase se debe NO se especifica
                                    ##el nombre de la clase se usa el parametro propio cls.


miobjeto=prueba("hola mundo")

miobjeto.metodo_clase()
print(miobjeto.respaldo)
miobjeto.respaldo="millos"
print(miobjeto.respaldo)

miobjeto.metodo_estatico()

miobjeto.metodo_clase()




