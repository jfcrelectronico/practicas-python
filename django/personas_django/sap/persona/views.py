from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from persona.forms import PersonaForm # se importa la clase personaform creada para no usar modelform_factory
from persona.models import Persona  # se importa la clase modelo Persona


<<<<<<< HEAD
def detallePersona(request,id):#no solo recibe la peticion si no el id de la persona de la cual se desea conocer la informacion
    #persona=Persona.objects.get(pk=id)# NO valida la existencia de un id valido por ello se usa el metodo get_object_or_404
=======
def detallePersona(request,id):
    #persona=Persona.objects.get(pk=id)
>>>>>>> 2b587631e83f5d369d661a56a3288c947193c05a
    persona=get_object_or_404(Persona,pk=id)# pk primary key en caso tal que la llave primaria no exista se genera un error de tipo 404
    return render(request,'personas/detallePersona.html',{'info_persona':persona})#con ctrl+D se duplican lineas


####modelform_factory se usa cuando no se tiene una clase propia de forms si no se crea el archivo forms y se edita luego se importa
#PersonaForm=modelform_factory(Persona, exclude=[])# se crea una clase PersonaForm a partir del metodo modelform_factory y se especifica la clase de modelo a utilizar
                                                  # No se excluye ningun campo
def nuevaPersona(request):#cuando se usa el recurso para crear agregar una persona se genera un metodo GET,pero cuando se va a enviar la info a la base de datos se generara un POST
    if request.method=='POST':#en este punto ya se debe procesar formulario enviandolo a la base de datos
        formaPersona=PersonaForm(request.POST)#se llena con la informacion del objeto request que contiene la informacion digitada en el formulario de ingreso
        if formaPersona.is_valid():#permite verificar si el formato del formulario es valido VERIFICAR PORQUE NO VALIDA
            formaPersona.save()#enviar la informacion a la base de datos
<<<<<<< HEAD
            return redirect('index')# una vez guarda la informacion se debe llevar la aplicacion a la pagina de inicio la etiqueta index se asigno en el arhivo urls para la pagina de bienvenida
=======
            return redirect('index')# una vez guarda la informacion se debe llevar la aplicacion a la pagina de inicio
>>>>>>> 2b587631e83f5d369d661a56a3288c947193c05a
        else:

            return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})#vuelve a cargar en la pagina de ingreso de datos los errores del formulario

    else:# se esta ingresando al template para digitar los datos del nuevo usuario
        formaPersona=PersonaForm()# se crea el objeto formaPersona a partir de la clase PersonaForm
        return render(request,'personas/nuevo.html',{'formaPersona':formaPersona})#el metodo render recibe el parametro request de peticion, luego la pagina/plantilla a la cual se va a dirigir
                                                                              # y finalmente la informacion respectiva a traves de un diccionario
<<<<<<< HEAD
                                                                              # el nombre del parametro valor del diccionario debe ser igual al de objeto modelo relacional del archivo nuevo.py

def editarPersona(request,id):#se recibe el parametro id con el cual se determinara cual es el registro a editar
    persona = get_object_or_404(Persona,pk=id)  # pk primary key en caso tal que la llave primaria no exista se genera un error de tipo 404, se recupera un objeto con id del tipo persona indicado
    if request.method=='POST':#en este punto ya se debe procesar formulario enviandolo a la base de datos
        formaPersona=PersonaForm(request.POST,instance=persona)#se llena con la informacion del objeto request que contiene la informacion digitada en el formulario de ingreso
        if formaPersona.is_valid():#permite verificar si el formato del formulario es valido xxxxxxxxxxxx VERIFICAR PORQUE NO VALIDA xxxxxxxxx
            formaPersona.save()#enviar la informacion a la base de datos no como create si no como update
            return redirect('index')# una vez guarda la informacion se debe llevar la aplicacion a la pagina de inicio
        else:
            return render(request, 'personas/editar.html', {'formaPersona': formaPersona})  # vuelve a cargar en la pagina de ingreso de datos los errores del formulario

    else:# se esta ingresando al template para digitar los datos del nuevo usuario

        formaPersona=PersonaForm(instance=persona)# se crea el objeto formaPersona a partir de la clase PersonaForm y se le envia el objeto persona con el id deseado para la modificacion
        return render(request,'personas/editar.html',{'formaPersona':formaPersona})#el metodo render recibe el parametro request de peticion, luego la pagina/plantilla a la cual se va a dirigir
                                                                              # y finalmente la informacion respectiva a traves de un diccionario
                                                                              # el nombre del parametro valor del diccionario debe ser igual al de objeto modelo relacional del archivo nuevo.py

def eliminarPersona(request,id):#se recibe el parametro id con el cual se determinara cual es el registro a editar
    persona = get_object_or_404(Persona,pk=id)  #obtener un objeto del id correspondiente o lanzar una error tipo 404
    if persona:
        persona.delete()#borrar el registro de la base de datos
    return redirect('index')#retornar a la pagina de inicio bienvenida y carga los valores de la base de datos
=======
                                                                              # el nombre del parametro valor del diccionario debe ser igual al de objeto modelo relacional del archivo nuevo.py
>>>>>>> 2b587631e83f5d369d661a56a3288c947193c05a
