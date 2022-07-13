from django.db import models

# Create your models here.
<<<<<<< HEAD
class Domicilio(models.Model):#la clase modelo extiende de la clase Model propia de django
=======
class Domicilio(models.Model):#la clase modelo extiende de la clase modelo
>>>>>>> 2b587631e83f5d369d661a56a3288c947193c05a
    calle=models.CharField(max_length=255)
    no_calle=models.IntegerField()
    pais=models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.no_calle} {self.pais}'# la llave primaria se genera en automatico por ello se llama self.id
                                                                               # asi no haga parte de las variables clase

class Persona (models.Model):
    Nombre=models.CharField(max_length=255) #A string field, for small- to large-sized strings.
                                            #For large amounts of text, use TextField.
    Apellido=models.CharField(max_length=255)
    Email=models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)#llave foranea para este caso se establece una relacion entre
                                                                                  #una persona y su domicilio(a traves de las clases),se debe especificar que sucede si se elimina
                                                                                  #un registro de la tabla de domicilio que este relacionada con un registro
                                                                                  # de la tabla de persona a ese parametro se le conoce
                                                                                  # como on_delete, y para poder asignarle un valor de
                                                                                  # null se debe indicar que el campo domicilio acepta un valor de null
                                                                                  #SI en on_delete=models.CASCADE se eliminaran tanto el registro de Domicilio como el de persona
<<<<<<< HEAD
    def __str__(self):# cuando se usa el metodo print en el llamada a un objeto mediente el metodo str se muestra el contenido o la informacion deseada y NO la direccion donde esta ubicado el objeto
=======
    def __str__(self):
>>>>>>> 2b587631e83f5d369d661a56a3288c947193c05a
        return f'Persona {self.id}:  {self.Nombre} {self.Apellido} {self.Email}'