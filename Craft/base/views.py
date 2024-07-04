from django.shortcuts import render
from .models import Articulos
from .forms import ArticulosForm

# Create your views here.
def Carrusel(request):
    articulos=Articulos.objects.all()
    return render(request,"base/Carrusel.html", {'articulos':articulos})

def registrar(request):
    if request.method == 'POST':
        form = ArticulosForm(request.POST, request.FILES)
        if form.is_valid(): #Si los datos recibidos son correctos
            form.save() #inserta
            return render(request,'base/ForCarrusel.html')
    form = ArticulosForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'base/ForCarrusel.html',{'form': form})



def contacto(request):
   return render(request,"base/ForCarrusel.html")