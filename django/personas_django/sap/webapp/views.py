from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from persona.models import Persona


def bienvenido(request):
    #return HttpResponse('hola mundo JFCR')
    #mensajes={'msg1':'primer mensaje'}
<<<<<<< HEAD
    no_personas=Persona.objects.count()#https://docs.djangoproject.com/en/3.2/ref/models/querysets/   # objects es un manejador que permite obtener informacion de la base de datos relacionada con una clase modelo, ademas count retorna la cantidad de registros actuales que tiene la base de datos
    #registros_db=Persona.objects.all()#https://docs.djangoproject.com/en/3.0/topics/db/queries/       # all es equivalente a ejecutar un comando sql-> select * from nombre_base_de_datos
    registros_db = Persona.objects.order_by('Nombre') #se mostraran todos los campos haciendo un query select * from nombre_base de datos order by  'parametro de referencia' por defecto se ordena de forma ascendete si se desea de forma descendente se debe agregar un simbolo menos antes de la etiqueta del parametro
    return render(request,'bienvenido.html',{'no_personas_bd':no_personas,'registros_act':registros_db})#el metodo render permite dibujar el contenido de una pagina y no solo texto plano como sucede con la respuesta return HttpResponse, se pasa al metodo tanto el archivo html como el diccionario creado
=======
    no_personas=Persona.objects.count()#https://docs.djangoproject.com/en/3.2/ref/models/querysets/
    registros_db=Persona.objects.all()#https://docs.djangoproject.com/en/3.0/topics/db/queries/
    return render(request,'bienvenido.html',{'no_personas_bd':no_personas,'registros_act':registros_db})#se pasa al metodo render tanto el archivo html como el diccionario creado
>>>>>>> 2b587631e83f5d369d661a56a3288c947193c05a
