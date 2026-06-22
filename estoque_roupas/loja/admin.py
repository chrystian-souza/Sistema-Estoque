from django.contrib import admin
from .models import Roupa, MovimentacaoEstoque, EstoqueAtual, Cliente, Pagamento, Debito, FluxoCaixa

admin.site.register(Roupa)
admin.site.register(MovimentacaoEstoque)
admin.site.register(EstoqueAtual)
admin.site.register(Cliente)
admin.site.register(Pagamento)
admin.site.register(Debito)
admin.site.register(FluxoCaixa)
