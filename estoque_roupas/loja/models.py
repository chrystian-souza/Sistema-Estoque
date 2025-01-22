from django.db import models
from django.utils import timezone



class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
   

class Roupa(models.Model):
    nome = models.CharField(max_length=100)
    tamanho = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nome} (Tamanho: {self.tamanho})'

class MovimentacaoEstoque(models.Model):
    TIPO_MOVIMENTACAO = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]

    roupa = models.ForeignKey(Roupa, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    tipo = models.CharField(max_length=7, choices=TIPO_MOVIMENTACAO)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.tipo.capitalize()} de {self.quantidade} {self.roupa.nome}'
    
class EstoqueAtual(models.Model):
    roupa = models.OneToOneField(Roupa, on_delete=models.CASCADE)
    quantidade_atual = models.PositiveIntegerField()

    def __str__(self):
        return f'Estoque de {self.roupa.nome}: {self.quantidade_atual}'
    

class Debito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='debitos')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Débito de {self.valor} por {self.cliente.nome}"

class FluxoCaixa(models.Model):
    data = models.DateField(auto_now_add=True)
    total_entrada = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_saida = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Fluxo de Caixa - {self.data}"
    
    def calcular_fluxo(self):
        return self.total_entrada - self.total_saida


from django.db import models

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'Pedido {self.id} - Cliente {self.cliente.nome}'



class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    roupa = models.ForeignKey(Roupa, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantidade}x {self.roupa.nome} - Pedido {self.pedido.id}'
    


class Debito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    numero_parcelas = models.PositiveIntegerField(default=0)
    parcelas_pagas = models.PositiveIntegerField(default=0)
    descricao = models.CharField(max_length=255, blank=True, null=True) 

    def __str__(self):
        return f'Débito de {self.cliente.nome} - Pedido {self.pedido.id}'
    
    def saldo_restante(self):
        return self.valor_total - self.valor_pago



class Pagamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)  # Se houver um pedido vinculado
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField(auto_now_add=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Pagamento de {self.valor_pago} para {self.cliente.nome}"
    


    