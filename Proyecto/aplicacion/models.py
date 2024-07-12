from django.db import models

# Create your models here.

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombres = models.CharField(max_length=20)
    apellidos= models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    contraseña =models.CharField(max_length=20)
    activo = models.IntegerField(default=1)
    def __str__(self):
        return str(self.nombres)+" "+str(self.apellidos)
    
    class Meta:
        ordering=['rut']
