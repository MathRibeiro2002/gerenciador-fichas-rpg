from django.shortcuts import render, redirect, get_object_or_404
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

def detalhes_ficha(request, id):
    ficha = get_object_or_404(Ficha, id=id)
    return render(request, 'fichas/detalhes_ficha.html', {'ficha': ficha})

@login_required(login_url='login')
def editar_ficha(request, id):
    ficha = get_object_or_404(Ficha, id=id, autor=request.user)
    if request.method == 'POST':
        form = FichaForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ficha atualizada com sucesso!')
            return redirect('detalhes_ficha', id=ficha.id)
    else:
        form = FichaForm(instance=ficha)
    return render(request, 'fichas/criar_ficha.html', {'form': form})

@login_required(login_url='login')
def deletar_ficha(request, id):
    ficha = get_object_or_404(Ficha, id=id, autor=request.user)
    if request.method == 'POST':
        ficha.delete()
        messages.success(request, 'Ficha deletada do sistema.')
        return redirect('home')
    return render(request, 'fichas/deletar_ficha.html', {'ficha': ficha})

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