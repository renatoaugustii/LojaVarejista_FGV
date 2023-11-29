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

# URL PARA PRODUTO
    path('produto/',views.produto, name='produto'),
    path('cadastrar_produto/',views.cadastrar_produto, name='cadastrar_produto'),
    path('excluir_produto/<int:produto_id>',views.excluir_produto, name='excluir_produto'),
    path('editar_produto/<int:produto_id>',views.editar_produto, name='editar_produto'),

    
# URL PARA FORNECEDOR
    path('fornecedor/',views.fornecedor, name='fornecedor'),
    path('cadastrar_fornecedor/',views.cadastrar_fornecedor, name='cadastrar_fornecedor'),
    path('excluir_fornecedor/<int:fornecedor_id>',views.excluir_fornecedor, name='excluir_fornecedor'),
    path('editar_fornecedor/<int:fornecedor_id>',views.editar_fornecedor, name='editar_fornecedor'),

# URL PARA LOJA
    path('loja/',views.loja, name='loja'),
    path('cadastrar_loja/',views.cadastrar_loja, name='cadastrar_loja'),
    path('excluir_loja/<int:loja_id>',views.excluir_loja, name='excluir_loja'),
    path('editar_loja/<int:loja_id>',views.editar_loja, name='editar_loja'),

]
