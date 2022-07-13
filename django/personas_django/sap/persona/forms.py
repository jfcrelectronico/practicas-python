from django.forms import ModelForm, EmailInput

from persona.models import Persona
<<<<<<< HEAD
#from models import Persona
=======

>>>>>>> 2b587631e83f5d369d661a56a3288c947193c05a

class PersonaForm(ModelForm):
    class Meta:
        model =Persona #se indica cual es la clase de modelo que se va a usar
        fields ='__all__'#cuales son los campos a usar, para este caso se van a usar todos del objeto modelo tipo persona
<<<<<<< HEAD
        #widgets tipo de campo del formulario tipo persona pero a nivel HTML estos permiten xxxxxxxxxVALIDARxxxxxxx que los datos ingresados en cada campo correspondan a un formato especifico https://docs.djangoproject.com/en/3.2/ref/forms/widgets/
        widgets = {
            'Email':EmailInput(attrs={'type':'email'})
            #'Email': EmailInput(attrs={'class': 'contact-form'})# Los atributos a evaluar deben tener la misma etiqueta incluyendo mayusculas y minusculas  que el archivo models y el render 0001_initial
        }
        #email=models.EmailInput()
=======
        #widgets tipo de campo del formulario tipo persona pero a nivel HTML estos permiten validar que los datos ingresados en cada campo correspondan a un formato especifico https://docs.djangoproject.com/en/3.2/ref/forms/widgets/
        widgets = {
            'email':EmailInput(attrs={'type':'email'})
        }
>>>>>>> 2b587631e83f5d369d661a56a3288c947193c05a
