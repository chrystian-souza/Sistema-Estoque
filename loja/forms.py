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
        fields = ['cliente', 'valor_pago', 'descricao']

class DebitoForm(forms.ModelForm):
    class Meta:
        model = Debito
        fields = ['pedido','valor_total','valor_pago','numero_parcelas', 'parcelas_pagas', 'descricao']  


class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['cliente', 'valor_pago', 'descricao']  # Use 'valor_pago' se for o nome correto no modelo

        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone',]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
          
        }

