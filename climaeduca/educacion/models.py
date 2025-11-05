from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    comuna = models.CharField(max_length=100)
    puntaje = models.IntegerField(default=0)
    racha = models.IntegerField(default=0)

class Pregunta(models.Model):
    texto = models.CharField(max_length=255)
    opcion_a = models.CharField(max_length=100)
    opcion_b = models.CharField(max_length=100)
    opcion_c = models.CharField(max_length=100)
    respuesta_correcta = models.CharField(max_length=1)  # 'A', 'B', 'C'

class RespuestaUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta_dada = models.CharField(max_length=1)
    es_correcta = models.BooleanField()
