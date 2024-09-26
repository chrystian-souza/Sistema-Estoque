from django import forms
from .models import Roupa, MovimentacaoEstoque

class RoupaForm(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ['nome', 'numero', 'preco', 'tamanho']

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoEstoque
        fields = ['roupa', 'quantidade', 'tipo']
