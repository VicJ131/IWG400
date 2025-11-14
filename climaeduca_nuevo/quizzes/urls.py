from django.urls import path
from . import views

app_name = 'quizzes'

urlpatterns = [
    path('diario/', views.quiz_diario, name='quiz_diario'),
    path('verificar-respuesta/', views.verificar_respuesta, name='verificar_respuesta'),
]