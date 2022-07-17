from django.shortcuts import render,redirect
from django.http import HttpResponse
from httplib2 import Http
from .forms import crear_banda,crear_estudio,crear_productor
from EstudiosMusicalesApp.models import Banda, Estudio, Productor


def index(request):
    return render(request,"EstudiosMusicalesApp/index.html",)

def estudios(request):
    estudios=Estudio.objects.all()
    ctx={"estudios":estudios}
    return render(request,'EstudiosMusicalesApp/estudios.html',ctx)

def productores(request):
    productores=Productor.objects.all()
    ctx={"productores":productores}
    return render(request,'EstudiosMusicalesApp/productores.html',ctx)
    pass

def bandas(request):
    bandas=Banda.objects.all()
    ctx={"bandas":bandas}
    return render(request,'EstudiosMusicalesApp/bandas.html',ctx)
    pass

def crear_estudio(request):
    
    
    if request.method == "POST":
        
        info_formulario = request.POST

        estudio=Estudio(nombre=info_formulario["nombre"], ubicacion=info_formulario["ubicacion"], cantidad_salas=int(info_formulario["cantidad_salas"]))

        estudio.save()
                        
        return redirect("estudios")
    
    else:
        return render(request,'EstudiosMusicalesApp/formulario_estudio.html',{})
    
    


def crear_productor(request):
    
    
    if request.method == "POST":
        
        info_formulario = request.POST

        productor=Productor(nombre=info_formulario["nombre"], apellido=info_formulario["apellido"], email=int(info_formulario["email"]))

        productor.save()
                        
        return redirect("productores")
    
    else:
        return render(request,'EstudiosMusicalesApp/formulario_productor.html',{})
    
    
def crear_banda(request):
    
    
    if request.method == "POST":
        
        info_formulario = request.POST

        banda=Banda(nombre=info_formulario["nombre"], genero=info_formulario["genero"], cantidad_salas=info_formulario["cantidad_salas"])

        banda.save()
                        
        return redirect("bandas")
    
    else:
        return render(request,'EstudiosMusicalesApp/formulario_banda.html',{})

    

def base (request):
    return render(request,'EstudiosMusicalesApp/base.html',{})