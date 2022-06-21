from django.shortcuts import render
from tienda.models import Producto

# Create your views here.

def tienda(request):
    producto = Producto.objects.all()
    return render(request, "tienda/tienda.html", {"producto": producto})