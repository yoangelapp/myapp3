from django import forms 

class FormularioContacto(forms.Form):
    nombre= forms.CharField(required=True, max_length= 20)
    email= forms.CharField( required=True, max_length=30)
    contenido= forms.CharField( required=True, max_length=100)
    