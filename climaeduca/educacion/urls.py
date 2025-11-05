from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro/', views.registro_usuario, name = 'registro'),
    path('', views.inicio, name='inicio'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]


from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.inicio, name='inicio'),
]
