from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from .models import Pregunta, QuizDiario, RespuestaUsuario, Categoria
import random

@login_required
def quiz_diario(request):
    """Vista principal del quiz diario"""
    # Por ahora, vista simple - luego implementamos la lógica completa
    preguntas = Pregunta.objects.all()[:5]  # 5 primeras preguntas
    
    return render(request, 'quizzes/quiz_diario.html', {
        'preguntas': preguntas,
    })

@login_required
def verificar_respuesta(request):
    """Vista para verificar respuestas (AJAX)"""
    if request.method == 'POST':
        pregunta_id = request.POST.get('pregunta_id')
        respuesta = request.POST.get('respuesta')
        
        pregunta = get_object_or_404(Pregunta, id=pregunta_id)
        es_correcta = (respuesta.upper() == pregunta.respuesta_correcta.upper())
        
        # Guardar respuesta
        respuesta_usuario = RespuestaUsuario(
            usuario=request.user,
            pregunta=pregunta,
            respuesta_dada=respuesta,
            es_correcta=es_correcta
        )
        respuesta_usuario.save()
        
        # Actualizar puntaje si es correcta
        if es_correcta:
            request.user.puntaje_total += 10
            request.user.save()
        
        return JsonResponse({
            'correcta': es_correcta,
            'explicacion': pregunta.explicacion,
            'puntaje_actual': request.user.puntaje_total
        })