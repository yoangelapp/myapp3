from django.shortcuts import render, HttpResponse



# Create your views here.

def home(request):
    
    return render(request, "home.html")

def sobre_nosotros(request):
    
    return render(request, "sobrenosotros.html")

def tienda(request):
    
    return render(request, "tienda.html")

def combustibles_alternos(request):
    
    return render(request, "combustible.html")

