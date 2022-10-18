import re
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages


def criar_cliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('usuario')
        password = request.POST.get('password')
        user = get_user_model()
        usuario = user(
            email=email,
            username=username,
    )
        usuario.set_password(password)
        usuario.save()
        messages.success(request, 'Usuario criado com sucesso')
        return redirect('clientes:login')
    ##print(f'{email} - {password}')
    return render(request, 'criar_clientes.html')


def login_user(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        user = authenticate(
        username=usuario,
        password=password

        )
        if user:
            login(request, user)
            messages.success(request, 'Usuario logado')
            return redirect('listar_acomodacoes')
        else:
            messages.error(request,'Usuario nao existe')
    return render(request, 'login.html')


def logout_user(request):
    return redirect(reverse('base.html'))
