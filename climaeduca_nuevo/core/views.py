from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser

def homepage(request):
    """Página principal pública - accesible sin login"""
    # Si el usuario YA está autenticado, redirigir al dashboard
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    
    # Si NO está autenticado, mostrar homepage pública
    return render(request, 'core/homepage.html')

@login_required
def dashboard(request):
    """Dashboard principal"""
    # Obtener top 5 usuarios para mostrar en dashboard
    top_usuarios = CustomUser.objects.order_by('-puntaje_total')[:5]
    
    # Posición del usuario actual en el ranking
    usuarios_por_encima = CustomUser.objects.filter(puntaje_total__gt=request.user.puntaje_total).count()
    posicion_ranking = usuarios_por_encima + 1
    
    return render(request, 'core/dashboard.html', {
        'top_usuarios': top_usuarios,
        'posicion_ranking': posicion_ranking,
    })

@login_required  
def ranking(request):
    """Página completa de ranking"""
    todos_usuarios = CustomUser.objects.order_by('-puntaje_total', '-racha_actual')
    
    # Encontrar posición del usuario actual
    usuarios_por_encima = CustomUser.objects.filter(puntaje_total__gt=request.user.puntaje_total).count()
    posicion_usuario = usuarios_por_encima + 1
    
    return render(request, 'core/ranking.html', {
        'usuarios': todos_usuarios,
        'posicion_usuario': posicion_usuario,
    })