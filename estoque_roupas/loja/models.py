from django.db import models
from django.utils import timezone

class Roupa(models.Model):
    nome = models.CharField(max_length=100)
    tamanho = models.CheckConstraint
    numero = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nome} (Tamanho: {self.numero})'

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
