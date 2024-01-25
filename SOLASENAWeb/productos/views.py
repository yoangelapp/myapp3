from django.shortcuts import render
from productos.models import producto 

# Create your views here.



def productos_asfalticos(request):
    
    productos=producto.objects.all()
    return render(request, "productosasfalticos.html", {"productos": productos})

def emulsiones_asfalticas(request):
    return render(request, "emulsionesasfalticas.html")