from django.db import models
from django.utils import timezone

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


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.nome

class Pagamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pagamentos')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Pagamento de {self.valor} por {self.cliente.nome}"

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
