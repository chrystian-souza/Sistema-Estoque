from django import forms
from .models import Roupa, MovimentacaoEstoque, Cliente, Pagamento, Debito

class RoupaForm(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ['nome', 'tamanho', 'preco']

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoEstoque
        fields = ['roupa', 'quantidade', 'tipo']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['cliente', 'valor', 'descricao']

class DebitoForm(forms.ModelForm):
    class Meta:
        model = Debito
        fields = ['cliente', 'valor', 'descricao']
