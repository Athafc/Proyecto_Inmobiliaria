from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

# Create your models here.

def validate_min_value(value):
    if value<0:
        raise ValidationError(
            'El valor deber ser positivo'
        )

class Usuario(models.Model):
    id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id_usuario.username

class Inmueble(models.Model):
    id_usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    id_tipo_inmueble = models.ForeignKey('Tipo_inmueble' , on_delete=models.CASCADE)
    id_comuna = models.ForeignKey('Comuna' , on_delete=models.CASCADE)
    id_region = models.ForeignKey('Region' , on_delete=models.CASCADE)
    nombre_inmueble =models.CharField(max_length=200)
    m2_construido = models.FloatField()
    numero_banos = models.PositiveBigIntegerField(default=0)
    numero_habitaciones = models.IntegerField(validators= [validate_min_value], default=0)
    direccion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre_inmueble



class Region(models.Model):
    region = models.TextField()

    def __str__(self):
        return self.region
    

class Comuna(models.Model):
    comuna = models.TextField()

    def __str__(self):
        return self.comuna
    

class Tipo_inmueble(models.Model):
    CHOICES = [
        ('Departamento', 'Departamento'),
        ('Casa', 'Casa'),
        ('Parcela', 'Parcela'),
    ]
    tipo = models.TextField(choices=CHOICES)

    def __str__(self):
        return self.tipo
    

class Tipo_usuario(models.Model):
    CHOICES = [
        ('Arrendador', 'Arrendador'),
        ('Arrendatario', 'Arrendatario')
    ]
    tipo = models.CharField(choices=CHOICES)

    def __str__(self):
        return self.tipo
  

class Perfil(models.Model):
    usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    tipo_usuario = models.ForeignKey('Tipo_usuario' , on_delete=models.CASCADE)
    rut = models.TextField()
    direccion = models.TextField()
    telefono = models.TextField()
    correo = models.EmailField()

    def __str__(self):
        return self.usuario.username

    