from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else: 
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def inicio(request):
    return render(request, 'inicio.html')
