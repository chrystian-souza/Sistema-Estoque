from django.shortcuts import render, redirect
from .models import Roupa, EstoqueAtual, MovimentacaoEstoque
from .forms import RoupaForm, MovimentacaoForm

def home(request):
    roupas = EstoqueAtual.objects.all()
    return render(request, 'loja/home.html', {'roupas': roupas})

def adicionar_roupa(request):
    if request.method == 'POST':
        form = RoupaForm(request.POST)
        if form.is_valid():
            roupa = form.save()
            EstoqueAtual.objects.create(roupa=roupa, quantidade_atual=0)
            return redirect('home')
    else:
        form = RoupaForm()
    return render(request, 'loja/adicionar_roupa.html', {'form': form})

def movimentar_estoque(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            movimentacao = form.save()
            estoque = EstoqueAtual.objects.get(roupa=movimentacao.roupa)
            if movimentacao.tipo == 'entrada':
                estoque.quantidade_atual += movimentacao.quantidade
            elif movimentacao.tipo == 'saida':
                estoque.quantidade_atual -= movimentacao.quantidade
            estoque.save()
            return redirect('home')
    else:
        form = MovimentacaoForm()
    return render(request, 'loja/movimentar_estoque.html', {'form': form})
