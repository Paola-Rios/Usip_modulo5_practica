from django.db import models
from django.conf import settings
#validadores
from .validators import validar_nombrePropietario 
from .validators import validar_carnetPropietario

class Propietario(models.Model):
    carnet = models.CharField(max_length=100,unique=True, validators=[validar_carnetPropietario]) 
    nombre = models.CharField(max_length=100, validators= [validar_nombrePropietario])
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=254)

    def __str__(self):
        return (" Carnet: - %s" % self.carnet)

class Departamento(models.Model):
    departamento_nombre = models.CharField(max_length=100, unique=True)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    bloque = models.CharField(max_length=100)
    costoExpensa = models.DecimalField(decimal_places=2, max_digits=10)
    fecha_Entrega = models.DateTimeField(auto_now=True)
    def __str__(self):
        return (" Departamento: - %s" % self.departamento_nombre)

class Expensa_Agua(models.Model):
    Id_Expensa_Agua = models.CharField(max_length=100, unique=True)
    Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    montoTotal = models.DecimalField(decimal_places=2, max_digits=10)
    cantidad_consumida = models.DecimalField(decimal_places=2, max_digits=10)
    mes = models.CharField(max_length=100)
    anio = models.CharField(max_length=100)
    estado = models.BooleanField(blank=True, default=True)

class Expensa(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    monto= models.DecimalField(decimal_places=2, max_digits=10)
    mes_Expensa= models.CharField(max_length=100)
    anio_Expensa= models.CharField(max_length=100)
    estado_Expensa = models.BooleanField(blank=False, default=False) 






