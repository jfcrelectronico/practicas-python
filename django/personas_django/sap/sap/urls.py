"""sap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

<<<<<<< HEAD
from persona.views import detallePersona,nuevaPersona,editarPersona,eliminarPersona
from webapp.views import bienvenido
=======
from webapp.views import bienvenido
from persona.views import detallePersona, nuevaPersona
>>>>>>> 2b587631e83f5d369d661a56a3288c947193c05a

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',bienvenido, name='index'),#pagina de inicio de la aplicacion con name puedo usar el metodo redirect para volver a esta
<<<<<<< HEAD

    #los nombres de los paths deben ser exactamente iguales a los asignados en los tags <a href: ></a> de la pagina bienvenidos html
    path('detalle_persona/<int:id>',detallePersona),#para recibir parametros en python se utiliza la sintaxis <>, el parametro especifica el tipo de
                                    #variable recibida y la etiqueta de la variable
    path('nueva_persona',nuevaPersona),
    path('editar_persona/<int:id>',editarPersona),
    path('eliminar_persona/<int:id>',eliminarPersona),
=======
    path('detalle_persona/<int:id>',detallePersona),#para recibir parametros en python se utiliza la sintaxis <>, el parametro especifica el tipo de
                                    #variable recibida y la etiqueta de la variable
    path('nueva_persona',nuevaPersona),
>>>>>>> 2b587631e83f5d369d661a56a3288c947193c05a
]
