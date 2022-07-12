from operator import index
from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('',index,name="index"),
    path('estudios/',estudios,name="estudios"),
    path('productores/',productores,name="productores"),
    path('bandas/',bandas,name="bandas"),
    path('crear_estudio/',crear_estudio,name="crear_estudio"),
    path('crear_productor/',crear_productor,name="crear_productor"),
    path('crear_banda/',crear_banda,name="crear_banda"),
    # path('base/',base,name="base"),
    
]