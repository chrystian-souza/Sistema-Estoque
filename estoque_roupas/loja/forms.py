from django import forms
from .models import Roupa, MovimentacaoEstoque

class RoupaForm(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ['nome', 'tamanho', 'preco', ]

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoEstoque
        fields = ['roupa', 'quantidade', 'tipo']
