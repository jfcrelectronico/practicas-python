from django.contrib import admin

# Register your models here.
from persona.models import Persona,Domicilio

<<<<<<< HEAD
#se agregan las clases modelo del sistema
admin.site.register(Persona) # clase modelo persona contienen nombre, apellido e email y comparte domicilio por herencia con la clase modelo Docimicilio
admin.site.register(Domicilio)# clase modelo Domicilio presenta herencia con la clase modelo Persona mediante llaves foraneas
=======

admin.site.register(Persona)
admin.site.register(Domicilio)
>>>>>>> 2b587631e83f5d369d661a56a3288c947193c05a
