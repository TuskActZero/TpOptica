from django.db import models
from datetime import datetime

class Paciente(models.Model):
    nombre = models.CharField('nombre',max_length=30)
    apellido = models.CharField('apellido',max_length=30)
    dni = models.IntegerField('dni')
    turno = models.ForeignKey('Turno', on_delete=models.CASCADE)
    historial_medico = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"el paciente {self.nombre}"

class Turno(models.Model):
    fecha = models.DateTimeField(verbose_name="fecha")

    def __str__(self):
        return f"la fecha del turno es {self.fecha}"


class Pedido(models.Model):
    nombre_producto = models.CharField(max_length=40)
    lejos = models.BooleanField(default=False)
    cerca = models.BooleanField(default=False)
    izquierda = models.BooleanField(default=False)
    derecha = models.BooleanField(default=False)
    armazon = models.BooleanField(default=False)
    id_lente = models.ForeignKey('Lente', on_delete=models.CASCADE)
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)
    pendiente = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_producto

class Lente(models.Model):
    nombre_lente = models.CharField(max_length=30)
    precio = models.IntegerField()

    def __str__(self):
            return self.nombre_lente