from django.urls import path, include
from . import views

urlpatterns = [

# URL PARA HOME
    path('',views.home, name='home'),
    path('home/',views.home, name='home'),

# URL PARA CLIENTES
    path('cliente/',views.cliente, name='cliente'),
    path('cadastrar_cliente/',views.cadastrar_cliente, name='cadastrar_cliente'),
    path('excluir_cliente/<int:cliente_id>',views.excluir_cliente, name='excluir_cliente'),
    path('editar_cliente/<int:cliente_id>',views.editar_cliente, name='editar_cliente'),

# URL PARA DEPENDENTE
    path('dependente/',views.dependente, name='dependente'),
    path('cadastrar_dependente/',views.cadastrar_dependente, name='cadastrar_dependente'),
    path('excluir_dependente/<int:dependente_id>',views.excluir_dependente, name='excluir_dependente'),
    path('editar_dependente/<int:dependente_id>',views.editar_dependente, name='editar_dependente'),

    path('produto/',views.produto, name='produto'),

    path('fornecedor/',views.fornecedor, name='fornecedor'),

    path('loja/',views.loja, name='loja'),
    path('cadastrar_loja/',views.cadastrar_loja, name='cadastrar_loja'),
    path('excluir_loja/<int:loja_id>',views.excluir_loja, name='excluir_loja'),
    path('editar_loja/<int:loja_id>',views.editar_loja, name='editar_loja'),


]
