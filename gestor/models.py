from email.policy import default
from django.db import models

# Create your models here.
class clientes(models.Model): 
    nombre = models.CharField(max_length=64)
    service = models.CharField(max_length=64)
    completado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre