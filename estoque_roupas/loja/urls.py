from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar_roupa/', views.adicionar_roupa, name='adicionar_roupa'),
    path('movimentar_estoque/', views.movimentar_estoque, name='movimentar_estoque'),
    path('estoque/', views.estoque_atual, name='estoque'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/excluir/<int:pk>/', views.excluir_cliente, name='excluir_cliente'),
    path('pagamentos/registrar/', views.registrar_pagamento, name='registrar_pagamento'),
    path('debitos/registrar/', views.registrar_debito, name='registrar_debito'),
    path('pedidos/', views.listar_pedidos, name='listar_pedidos'),
    path('pedido/<int:pedido_id>/', views.detalhes_pedido, name='detalhes_pedido'),
    path('pedido/adicionar/', views.adicionar_pedido, name='adicionar_pedido'),
    path('debitos/', views.listar_debitos, name='listar_debitos'),
    path('debito/<int:debito_id>/', views.detalhes_debito, name='detalhes_debito'),
    path('debito/<int:debito_id>/pagamento/', views.adicionar_pagamento, name='adicionar_pagamento'),
    path('debito/<int:debito_id>/pagamentos/', views.listar_pagamentos, name='listar_pagamentos'),
]