from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)

class Inmueble(models.Model):
    id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    id_tipo_inmueble = models.ForeignKey('Tipo_inmueble' , on_delete=models.CASCADE)
    id_comuna = models.ForeignKey('Comuna' , on_delete=models.CASCADE)
    id_region = models.ForeignKey('Region' , on_delete=models.CASCADE)
    nombre_inmueble =models.CharField(max_length=200)
    m2_construido = models.FloatField()
    numero_banos = models.IntegerField(validators= [MinValueValidator(0)], default=0)
    numero_habitaciones = models.IntegerField(validators= [MinValueValidator(0)], default=0)
    direccion = models.CharField(max_length=200)


class Region(models.Model):
    region = models.TextField()
    

class Comuna(models.Model):
    comuna = models.TextField()
    

class Tipo_inmueble(models.Model):
    CHOICES = [
        ('Departamento', 'Departamento'),
        ('Casa', 'Casa'),
        ('Parcela', 'Parcela'),
    ]
    tipo = models.TextField(choices=CHOICES)
    

class Tipo_usuario(models.Model):
    CHOICES = [
        ('Arrendador', 'Arrendador'),
        ('Arrendatario', 'Arrendatario')
    ]
    tipo = models.CharField(choices=CHOICES)
  

class Perfil(models.Model):
    usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    rut = models.TextField()
    direccion = models.TextField()
    telefono = models.TextField()
    correo = models.EmailField()

    