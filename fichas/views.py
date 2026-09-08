from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Ficha
from .forms import FichaForm, CadastroForm

def home(request):
    query = request.GET.get('busca') 
    
    if query:
        fichas = Ficha.objects.filter(is_publica=True, nome_personagem__icontains=query)
    else:
        fichas = Ficha.objects.filter(is_publica=True)
        
    return render(request, 'fichas/home.html', {'fichas': fichas, 'query': query})

@login_required(login_url='login')
def criar_ficha(request):
    if request.method == 'POST':
        form = FichaForm(request.POST)
        if form.is_valid():
            ficha = form.save(commit=False)
            ficha.autor = request.user
            ficha.save()
            messages.success(request, 'Ficha criada com sucesso!')
            return redirect('home')
    else:
        form = FichaForm()
        
    return render(request, 'fichas/criar_ficha.html', {'form': form})

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('home')
    else:
        form = CadastroForm()
    
    return render(request, 'fichas/cadastro.html', {'form': form})