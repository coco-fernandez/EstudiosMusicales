from django.db import models



class Estudio(models.Model):
    nombre=models.CharField(max_length=30)
    ubicacion=models.CharField(max_length=30)
    cantidad_salas=models.IntegerField()
    

class Banda(models.Model):
    nombre=models.CharField(max_length=30)
    genero=models.CharField(max_length=30)
    cantidad_integrantes=models.IntegerField()
    

class Productor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    
    class Meta:
        verbose_name_plural="Productores"
    


