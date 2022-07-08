from django.shortcuts import render
from django.http import HttpResponse

from EstudiosMusicalesApp.models import Banda, Estudio, Productor


def index(request):
    return render(request,"EstudiosMusicalesApp/index.html",)

def estudios(request):
    estudios=Estudio.objects.all()
    ctx={"estudios":estudios}
    return render(request,'ProyectoCoderApp/estudios.html',ctx)
    pass

def productores(request):
    productores=Productor.objects.all()
    ctx={"productores":productores}
    return render(request,'ProyectoCoderApp/productores.html',ctx)
    pass

def bandas(request):
    bandas=Banda.objects.all()
    ctx={"bandas":bandas}
    return render(request,'ProyectoCoderApp/bandas.html',ctx)
    pass

