from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adicionar/', views.adicionar_roupa, name='adicionar_roupa'),
    path('movimentar/', views.movimentar_estoque, name='movimentar_estoque'),
]
