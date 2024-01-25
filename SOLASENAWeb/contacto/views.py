from django.shortcuts import render, redirect
from .forms import FormularioContacto
from .models import contactanos
from django.core.mail import EmailMessage

# Create your views here.


def contacto(request):
   formulario_contacto= contactanos.objects.all()
   return render(request, "contacto.html", {'mi_formulario':formulario_contacto})

def registrarFormC(request):

   
   nombre=request.POST['txtNombre']
   mail=request.POST['txtMail']
   contenido=request.POST['txtContenido']

   Contactanos = contactanos.objects.create(nombre=nombre, mail=mail, contenido=contenido)
   
   email=EmailMessage("MENSAJE DESDE TU PAGINA WEB SOLASENA.COM",
   "El usuario con nombre {} con la direccion de correo {} te dejo el siguiente mensaje:\n\n {}".format(nombre,mail,contenido),"",
   ["yoangelfc@gmail.com"],reply_to=[mail])

   try:
      email.send()
      return redirect('/SolasenaWebApp/contacto/?valido')
   except:
      return redirect('/SolasenaWebApp/contacto/?novalido')
   
