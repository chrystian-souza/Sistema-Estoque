from django.shortcuts import render, get_object_or_404, redirect
from .models import Roupa, EstoqueAtual, MovimentacaoEstoque, Cliente, Pagamento, Debito
from .forms import RoupaForm, MovimentacaoForm, ClienteForm, PagamentoForm, DebitoForm


# Home
def home(request):
    roupas = EstoqueAtual.objects.all()
    return render(request, 'loja/home.html', {'roupas': roupas})

# Adicionar roupa
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

# Movimentar estoque
def movimentar_estoque(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            movimentacao = form.save()
            estoque = EstoqueAtual.objects.get(roupa=movimentacao.roupa)
            if movimentacao.tipo == 'entrada':
                estoque.quantidade_atual += movimentacao.quantidade
            elif movimentacao.tipo == 'saida':
                if estoque.quantidade_atual >= movimentacao.quantidade:  # Verificar se há estoque suficiente
                    estoque.quantidade_atual -= movimentacao.quantidade
                else:
                    # Pode ser interessante adicionar um aviso ao usuário
                    pass  # Adicione lógica para lidar com estoque insuficiente
            estoque.save()
            return redirect('home')
    else:
        form = MovimentacaoForm()
    return render(request, 'loja/movimentar_estoque.html', {'form': form})

# Listar clientes
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'loja/listar_clientes.html', {'clientes': clientes})


# Adicionar cliente
def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'loja/adicionar_clientes.html', {'form': form})

# Editar cliente
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'loja/editar_cliente.html', {'form': form})

# Excluir cliente
def excluir_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'loja/excluir_cliente.html', {'cliente': cliente})

# Estoque Atual
def estoque_atual(request):
    estoques = EstoqueAtual.objects.all()  # Obter todos os registros de EstoqueAtual
    return render(request, 'loja/estoque.html', {'estoques': estoques})

# Registrar pagamento
def registrar_pagamento(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PagamentoForm()
    return render(request, 'loja/registrar_pagamento.html', {'form': form})

# Registrar débito
def registrar_debito(request):
    if request.method == 'POST':
        form = DebitoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DebitoForm()
    return render(request, 'loja/registrar_debito.html', {'form': form})



from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido, Debito, Pagamento
from .forms import PagamentoForm

def listar_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'loja/listar_pedidos.html', {'pedidos': pedidos})

def detalhes_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'loja/detalhes_pedido.html', {'pedido': pedido})

def listar_debitos(request):
    debitos = Debito.objects.all()
    return render(request, 'loja/listar_debitos.html', {'debitos': debitos})

def detalhes_debito(request, debito_id):
    debito = get_object_or_404(Debito, id=debito_id)
    return render(request, 'loja/detalhes_debito.html', {'debito': debito})

def adicionar_pagamento(request, debito_id):
    debito = get_object_or_404(Debito, id=debito_id)
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            pagamento = form.save(commit=False)
            pagamento.debito = debito
            pagamento.save()
            debito.valor_pago += pagamento.valor_pago
            debito.parcelas_pagas += 1
            debito.save()
            return redirect('detalhes_debito', debito_id=debito.id)
    else:
        form = PagamentoForm()
    return render(request, 'loja/adicionar_pagamento.html', {'form': form, 'debito': debito})

def listar_pagamentos(request, debito_id):
    debito = get_object_or_404(Debito, id=debito_id)
    pagamentos = Pagamento.objects.filter(debito=debito)
    return render(request, 'loja/listar_pagamentos.html', {'pagamentos': pagamentos, 'debito': debito})



def adicionar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')  # Redirecione para uma lista de pedidos, ou outro local
    else:
        form = PedidoForm()
    
    return render(request, 'loja/adicionar_pedido.html', {'form': form})

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')  # Redireciona para a página de listagem de clientes após o cadastro
    else:
        form = ClienteForm()
    return render(request, 'cadastrar_cliente.html', {'form': form})