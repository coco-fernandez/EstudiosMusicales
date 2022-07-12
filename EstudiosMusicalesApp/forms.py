from django import forms

class crear_estudio(forms.Form):
    nombre=forms.CharField(max_length=30)
    ubicacion=forms.CharField(max_length=30)
    cantidad_salas=forms.IntegerField()
    
class crear_banda(forms.Form):
    nombre=forms.CharField(max_length=30,label="Nombre")
    genero=forms.CharField(max_length=30,label="Género")
    cantidad_integrantes=forms.IntegerField(max_length=10)
    
class crear_productor(forms.Form):
    nombre=forms.CharField(max_length=30,label="Nombre")
    apellido=forms.CharField(max_length=30,label="Apellido")
    email=forms.EmailField()