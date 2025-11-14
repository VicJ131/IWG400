from django.db import models
from django.conf import settings

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre

class Pregunta(models.Model):
    DIFICULTAD_CHOICES = [
        ('facil', 'Fácil'),
        ('medio', 'Medio'), 
        ('dificil', 'Difícil'),
    ]
    
    texto = models.CharField(max_length=255)
    opcion_a = models.CharField(max_length=100)
    opcion_b = models.CharField(max_length=100)
    opcion_c = models.CharField(max_length=100)
    respuesta_correcta = models.CharField(max_length=1)  # A, B, C
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    dificultad = models.CharField(max_length=10, choices=DIFICULTAD_CHOICES, default='facil')
    explicacion = models.TextField(blank=True)
    
    def __str__(self):
        return self.texto[:50]

class QuizDiario(models.Model):
    fecha = models.DateField(auto_now_add=True)
    preguntas = models.ManyToManyField(Pregunta)
    activo = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ['fecha']
    
    def __str__(self):
        return f"Quiz del {self.fecha}"

class RespuestaUsuario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta_dada = models.CharField(max_length=1)
    es_correcta = models.BooleanField()
    fecha_respuesta = models.DateTimeField(auto_now_add=True)
    quiz_diario = models.ForeignKey(QuizDiario, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        unique_together = ['usuario', 'pregunta', 'quiz_diario']

    def __str__(self):
        return f"{self.usuario.username} - {self.pregunta.texto[:30]}"