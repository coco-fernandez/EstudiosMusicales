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
    
    return render(request,'EstudiosMusicalesApp/formulario_estudio.html',{})





    # if request.method=="POST":    #post
        
    #     formulario=crear_estudio(request.POST)
         
    #     if formulario.is_valid():
            
    #         info_estudio=formulario.cleaned_data
        
    #         estudio=Estudio(nombre=info_estudio["nombre"],ubicacion=info_estudio["ubicacion"],cantidad_salas=info_estudio["cantidad_salas"])
            
    #         estudio.save()    #guarda en la DB
            
    #         return redirect("estudios")
        
    #     else:
    #         return render(request,'EstudiosMusicalesApp/crear_estudio.html',{"form":formulario})
    
    # else:
    #     formulario=crear_estudio()
        
    #     return render(request,'EstudiosMusicalesApp/crear_estudio.html',{"form":formulario})

def crear_productor(request):
    pass

def crear_banda(request):
    pass

def base (request):
    return render(request,'EstudiosMusicalesApp/base.html',{})