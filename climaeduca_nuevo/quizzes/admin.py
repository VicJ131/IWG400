from django.contrib import admin
from .models import Categoria, Pregunta, QuizDiario, RespuestaUsuario

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']

@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ['texto', 'categoria', 'dificultad', 'respuesta_correcta']
    list_filter = ['categoria', 'dificultad']
    search_fields = ['texto']

@admin.register(QuizDiario)
class QuizDiarioAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'activo']
    list_filter = ['fecha', 'activo']

@admin.register(RespuestaUsuario)
class RespuestaUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'pregunta', 'respuesta_dada', 'es_correcta', 'fecha_respuesta']
    list_filter = ['es_correcta', 'fecha_respuesta']