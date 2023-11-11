from django.contrib import admin
from .models import tab_cliente, tab_dependente, tab_loja, tab_produto, tab_pedido, tab_item, tab_fornecedor

class ListViewCliente(admin.ModelAdmin):
    list_display=('nomeCliente', 'cpf', 'telefone')

# Register your models here.
admin.site.register(tab_cliente, ListViewCliente)
admin.site.register(tab_dependente)
admin.site.register(tab_pedido)
admin.site.register(tab_loja)
admin.site.register(tab_produto)
admin.site.register(tab_fornecedor)
admin.site.register(tab_item)