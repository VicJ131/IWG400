from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    comuna = models.CharField(max_length=100, blank=True, default="")
    puntaje_total = models.IntegerField(default=0)
    racha_actual = models.IntegerField(default=0)
    ultima_conexion = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.username