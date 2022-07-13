from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Gerencia(models.Model):
    nombre_gerencia= models.CharField(max_length=30)
    director= models.CharField(max_length=40)
    cant_empleados= models.IntegerField()
    
    def __str__(self):
        return f" {self.nombre_gerencia}"





class Areas(models.Model):
    nombre_sector= models.CharField(max_length=30)
    cant_empleados= models.IntegerField()
    puestos_vacantes= models.IntegerField()

    def __str__(self):
        return f"Sector: {self.nombre_sector} - Empleados: {self.cant_empleados} - Vacantes: {self.puestos_vacantes}"


class Empleados(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    area= models.CharField(max_length=30)
    fecha_ingreso=models.DateField()

    def __str__(self):
        return f"Apellido: {self.apellido} - Nombre: {self.nombre}"

class Vacaciones(models.Model):
    fecha_solicitud= models.DateField()
    solicitante= models.CharField(max_length=20)
    inicio_vacaciones= models.DateField()
    fin_vacaciones= models.DateField()


class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='avatares',null=True, blank =True)
