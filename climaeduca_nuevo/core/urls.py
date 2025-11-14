from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='homepage'),           # ← Pública
    path('dashboard/', views.dashboard, name='dashboard'), # ← Privada
    path('ranking/', views.ranking, name='ranking'),       # ← Privada
]